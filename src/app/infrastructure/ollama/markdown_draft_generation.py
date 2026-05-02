from __future__ import annotations

import json
import re
from dataclasses import dataclass
from urllib import error, request

from ...domain.markdown_draft import (
    ReferenceEnrichment,
    ReferenceSuggestion,
    TranscriptIdea,
    build_excerpt,
)
from ...domain.content_classification import TranscriptIdeaClassifier
from ...domain.models import ContentFamily, VideoSubmission

MAX_PROMPT_WORDS = 80
MAX_SUMMARY_WORDS = 80
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"


@dataclass(slots=True)
class OllamaTranscriptIdeaExtractor:
    model: str = "llama3"
    timeout_seconds: float = 60.0
    max_prompt_words: int = MAX_PROMPT_WORDS

    def extract(self, submission: VideoSubmission) -> TranscriptIdea:
        prompt = _idea_prompt(submission, self.max_prompt_words)
        try:
            payload = _load_json_object(_run_ollama(self.model, prompt, self.timeout_seconds))
            return TranscriptIdea(
                title=_required_text(payload, "title"),
                summary=_required_text(payload, "summary"),
                editorial_angle=_required_text(payload, "editorial_angle"),
                candidate_family=ContentFamily[
                    _required_text(payload, "candidate_family").upper()
                ],
                rationale=_required_text(payload, "rationale"),
            )
        except (RuntimeError, ValueError, TimeoutError, OSError):
            return _fallback_idea(submission)


@dataclass(slots=True)
class OllamaReferenceEnricher:
    model: str = "llama3"
    timeout_seconds: float = 60.0
    max_prompt_words: int = MAX_PROMPT_WORDS

    def enrich(
        self,
        submission: VideoSubmission,
        idea: TranscriptIdea,
    ) -> ReferenceEnrichment:
        prompt = _reference_prompt(submission, idea, self.max_prompt_words)
        try:
            payload = _load_json_object(_run_ollama(self.model, prompt, self.timeout_seconds))
            references = tuple(
                ReferenceSuggestion(
                    title=_required_text(reference, "title"),
                    support_note=_required_text(reference, "support_note"),
                    url=_optional_text(reference, "url"),
                    source_hint=_optional_text(reference, "source_hint"),
                )
                for reference in _required_sequence(payload, "references")
            )
            return ReferenceEnrichment(
                references=references,
                note=_optional_text(payload, "note") or "",
            )
        except (RuntimeError, ValueError, TimeoutError, OSError):
            return ReferenceEnrichment(
                references=(),
                note="reference enrichment fell back to an empty set after local model failure or timeout",
            )


def _run_ollama(model: str, prompt: str, timeout_seconds: float) -> str:
    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": False,
        },
        ensure_ascii=False,
    ).encode("utf-8")
    req = request.Request(
        OLLAMA_API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=timeout_seconds) as response:
            body = response.read().decode("utf-8")
    except error.URLError as exc:  # pragma: no cover - environment dependent
        if isinstance(getattr(exc, "reason", None), TimeoutError):
            raise TimeoutError("ollama request timed out") from exc
        raise RuntimeError(f"ollama request failed: {exc.reason}") from exc
    except TimeoutError as exc:  # pragma: no cover - environment dependent
        raise TimeoutError("ollama request timed out") from exc

    try:
        response_payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise ValueError(f"could not parse JSON response from ollama: {body!r}") from exc

    if not isinstance(response_payload, dict):
        raise ValueError("ollama response must be a JSON object")

    response_text = response_payload.get("response")
    if not isinstance(response_text, str):
        raise ValueError("ollama response missing text content")
    return response_text.strip()


def _load_json_object(text: str) -> dict[str, object]:
    candidate = _extract_json_fragment(text)
    try:
        payload = json.loads(candidate)
    except json.JSONDecodeError as exc:
        raise ValueError(f"could not parse JSON from ollama output: {text!r}") from exc

    if not isinstance(payload, dict):
        raise ValueError("ollama output must be a JSON object")
    return payload


def _extract_json_fragment(text: str) -> str:
    match = re.search(r"\{.*\}", text, flags=re.DOTALL)
    if match is None:
        raise ValueError(f"could not find JSON object in ollama output: {text!r}")
    return match.group(0)


def _idea_prompt(submission: VideoSubmission, max_words: int) -> str:
    summary = _transcript_summary(submission.transcript.text, max_words)
    return "\n".join(
        [
            "You extract one markdown draft idea from a transcript.",
            "Return JSON only with keys: title, summary, editorial_angle, candidate_family, rationale.",
            "candidate_family must be one of EPISODE, CONCEPT, REFERENCE, NOTE.",
            "",
            f"Title: {submission.title or '(untitled)'}",
            f"Video ID: {submission.video_id}",
            f"Metadata: {json.dumps(dict(sorted(submission.metadata.items())), ensure_ascii=False)}",
            f"Transcript summary length: {len(summary.split())} words",
            "",
            "Transcript summary:",
            summary,
        ]
    )


def _reference_prompt(
    submission: VideoSubmission,
    idea: TranscriptIdea,
    max_words: int,
) -> str:
    summary = _transcript_summary(submission.transcript.text, max_words)
    return "\n".join(
        [
            "You enrich a transcript-derived idea with references.",
            "Return JSON only with keys: references, note.",
            "references must be a list of objects with title, support_note, url, source_hint.",
            "Use null for url when there is no stable link.",
            "",
            f"Idea title: {idea.title}",
            f"Idea summary: {idea.summary}",
            f"Editorial angle: {idea.editorial_angle}",
            f"Candidate family: {idea.candidate_family.value}",
            "",
            f"Source title: {submission.title or '(untitled)'}",
            f"Video ID: {submission.video_id}",
            f"Transcript summary length: {len(summary.split())} words",
            "",
            "Transcript summary:",
            summary,
        ]
    )


def _transcript_summary(text: str, max_words: int) -> str:
    cleaned_lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if _looks_like_srt_index(line) or _looks_like_timestamp(line):
            continue
        cleaned_lines.append(line)

    cleaned_text = " ".join(cleaned_lines) if cleaned_lines else text
    words = cleaned_text.split()
    summary = " ".join(words[:max_words])
    return summary if len(words) <= max_words else f"{summary}..."


def _looks_like_srt_index(line: str) -> bool:
    return line.isdigit()


def _looks_like_timestamp(line: str) -> bool:
    return "-->" in line


def _fallback_idea(submission: VideoSubmission) -> TranscriptIdea:
    classifier = TranscriptIdeaClassifier()
    recommendation = classifier.classify(submission)
    summary = build_excerpt(submission.transcript, limit=32)
    title = submission.title or "Transcript Draft"
    editorial_angle = (
        "AI and software development as a practical working pair"
        if "ia" in submission.transcript.text.lower() or "inteligência artificial" in submission.transcript.text.lower()
        else "A reflective transcript that should become a readable markdown draft"
    )
    return TranscriptIdea(
        title=title,
        summary=summary,
        editorial_angle=editorial_angle,
        candidate_family=recommendation.family,
        rationale="local fallback used after Ollama timeout or parse failure",
    )


def _required_text(payload: dict[str, object], key: str) -> str:
    value = payload.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"missing or invalid {key!r} in ollama output")
    return value.strip()


def _optional_text(payload: dict[str, object], key: str) -> str | None:
    value = payload.get(key)
    if value is None:
        return None
    if not isinstance(value, str):
        raise ValueError(f"invalid {key!r} in ollama output")
    text = value.strip()
    return text or None


def _required_sequence(payload: dict[str, object], key: str) -> list[dict[str, object]]:
    value = payload.get(key)
    if not isinstance(value, list):
        raise ValueError(f"missing or invalid {key!r} in ollama output")

    items: list[dict[str, object]] = []
    for item in value:
        if not isinstance(item, dict):
            raise ValueError(f"invalid item in {key!r} from ollama output")
        items.append(item)
    return items
