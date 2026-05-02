from __future__ import annotations

import re
import unicodedata

from .models import ContentFamily, ContentFamilyRecommendation, VideoSubmission


REFERENCE_CUES: tuple[tuple[str, str], ...] = (
    ("community guidelines", "community guidelines are the main source"),
    ("official", "official source language points to references"),
    ("documentation", "documentation language points to references"),
    ("documentacao", "documentacao language points to references"),
    ("policy", "policy language points to references"),
    ("reference", "reference language points to references"),
    ("referencia", "referencia language points to references"),
    ("source", "source language points to references"),
    ("according to", "attribution language points to references"),
    ("fonte", "fonte language points to references"),
    ("oficial", "oficial language points to references"),
    ("segundo", "segundo language points to references"),
    ("conforme", "conforme language points to references"),
)

NOTE_CUES: tuple[tuple[str, str], ...] = (
    ("workflow", "workflow language points to notes"),
    ("checklist", "checklist language points to notes"),
    ("step by step", "step-by-step language points to notes"),
    ("steps", "step language points to notes"),
    ("process", "process language points to notes"),
    ("procedure", "procedure language points to notes"),
    ("passo a passo", "passo a passo language points to notes"),
    ("fluxo", "fluxo language points to notes"),
    ("processo", "processo language points to notes"),
    ("procedimento", "procedimento language points to notes"),
    ("etapas", "etapas language points to notes"),
    ("manual", "manual guidance points to notes"),
)

CONCEPT_CUES: tuple[tuple[str, str], ...] = (
    ("principle", "principle language points to concepts"),
    ("boundary", "boundary language points to concepts"),
    ("distinction", "distinction language points to concepts"),
    ("model", "model language points to concepts"),
    ("meaning", "meaning language points to concepts"),
    ("why it matters", "explanatory framing points to concepts"),
    ("principio", "principio language points to concepts"),
    ("limite", "limite language points to concepts"),
    ("fronteira", "fronteira language points to concepts"),
    ("significado", "significado language points to concepts"),
    ("por que importa", "por que importa language points to concepts"),
)


class TranscriptIdeaClassifier:
    def classify(self, submission: VideoSubmission) -> ContentFamilyRecommendation:
        haystack = _normalize(f"{submission.title or ''} {submission.transcript.text}")

        match = _first_match(haystack, REFERENCE_CUES)
        if match is not None:
            cue, reason = match
            return ContentFamilyRecommendation(
                family=ContentFamily.REFERENCE,
                matched_cue=cue,
                reason=reason,
            )

        match = _first_match(haystack, NOTE_CUES)
        if match is not None:
            cue, reason = match
            return ContentFamilyRecommendation(
                family=ContentFamily.NOTE,
                matched_cue=cue,
                reason=reason,
            )

        match = _first_match(haystack, CONCEPT_CUES)
        if match is not None:
            cue, reason = match
            return ContentFamilyRecommendation(
                family=ContentFamily.CONCEPT,
                matched_cue=cue,
                reason=reason,
            )

        return ContentFamilyRecommendation(
            family=ContentFamily.EPISODE,
            matched_cue="default",
            reason="no stronger family cue detected; default to episode",
        )


def _first_match(
    haystack: str,
    cues: tuple[tuple[str, str], ...],
) -> tuple[str, str] | None:
    for cue, reason in cues:
        if re.search(_cue_pattern(cue), haystack):
            return cue, reason
    return None


def _normalize(text: str) -> str:
    decomposed = unicodedata.normalize("NFKD", text.lower())
    without_accents = "".join(
        character
        for character in decomposed
        if not unicodedata.combining(character)
    )
    return " ".join(without_accents.split())


def _cue_pattern(cue: str) -> str:
    escaped = re.escape(_normalize(cue))
    return rf"\b{escaped}\b"
