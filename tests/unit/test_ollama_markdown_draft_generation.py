from __future__ import annotations

import pytest

from app.domain.models import Transcript, VideoSubmission
from app.infrastructure.ollama.markdown_draft_generation import (
    OllamaReferenceEnricher,
    OllamaTranscriptIdeaExtractor,
)


class _FakeResponse:
    def __init__(self, body: str) -> None:
        self._body = body.encode("utf-8")

    def __enter__(self) -> "_FakeResponse":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        return None

    def read(self) -> bytes:
        return self._body


def test_ollama_prompts_are_truncated_before_execution(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, str] = {}

    def fake_urlopen(request_obj, timeout):  # type: ignore[no-untyped-def]
        captured["body"] = request_obj.data.decode("utf-8")
        assert request_obj.full_url == "http://127.0.0.1:11434/api/generate"
        assert timeout == 3.0
        return _FakeResponse(
            '{"response":"{\\"title\\":\\"Draft\\",\\"summary\\":\\"Summary\\",\\"editorial_angle\\":\\"Angle\\",\\"candidate_family\\":\\"EPISODE\\",\\"rationale\\":\\"Reason\\"}"}'
        )

    monkeypatch.setattr(
        "app.infrastructure.ollama.markdown_draft_generation.request.urlopen",
        fake_urlopen,
    )

    transcript_words = [f"word{i}" for i in range(1, 401)]
    submission = VideoSubmission(
        video_id="video-long",
        title="Long transcript",
        transcript=Transcript(" ".join(transcript_words)),
    )

    result = OllamaTranscriptIdeaExtractor(timeout_seconds=3.0).extract(submission)

    assert result.title == "Draft"
    assert "word181" not in captured["body"]
    assert "Transcript summary length: 80 words" in captured["body"]
    assert "00:00:" not in captured["body"]
    assert "Transcript summary:" in captured["body"]


def test_ollama_timeout_falls_back_to_local_draft(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_urlopen(request_obj, timeout):  # type: ignore[no-untyped-def]
        raise TimeoutError

    monkeypatch.setattr(
        "app.infrastructure.ollama.markdown_draft_generation.request.urlopen",
        fake_urlopen,
    )

    submission = VideoSubmission(
        video_id="video-timeout",
        title="Software and AI",
        transcript=Transcript(
            "Eu tenho pensado sobre desenvolvimento de software e inteligência artificial."
        ),
    )

    idea = OllamaTranscriptIdeaExtractor(timeout_seconds=0.01).extract(submission)
    enrichment = OllamaReferenceEnricher(timeout_seconds=0.01).enrich(submission, idea)

    assert idea.title == "Software and AI"
    assert idea.rationale == "local fallback used after Ollama timeout or parse failure"
    assert "practical working pair" in idea.editorial_angle
    assert enrichment.references == ()
    assert "fell back to an empty set" in enrichment.note
