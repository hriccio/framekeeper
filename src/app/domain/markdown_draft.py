from __future__ import annotations

from dataclasses import dataclass

from .models import ContentFamily, Transcript, VideoSubmission


@dataclass(frozen=True, slots=True)
class TranscriptIdea:
    title: str
    summary: str
    editorial_angle: str
    candidate_family: ContentFamily
    rationale: str


@dataclass(frozen=True, slots=True)
class ReferenceSuggestion:
    title: str
    support_note: str
    url: str | None = None
    source_hint: str | None = None


@dataclass(frozen=True, slots=True)
class ReferenceEnrichment:
    references: tuple[ReferenceSuggestion, ...]
    note: str = ""


@dataclass(frozen=True, slots=True)
class MarkdownDraft:
    submission: VideoSubmission
    idea: TranscriptIdea
    references: tuple[ReferenceSuggestion, ...]
    transcript_excerpt: str
    source_metadata: tuple[tuple[str, str], ...] = ()
    enrichment_note: str = ""

    def to_markdown(self) -> str:
        lines = [
            "# Markdown Draft",
            "",
            f"- Video ID: {self.submission.video_id}",
            f"- Source title: {self.submission.title or '(untitled)'}",
            f"- Candidate family: {self.idea.candidate_family.value}",
            f"- Editorial angle: {self.idea.editorial_angle}",
            f"- Rationale: {self.idea.rationale}",
            "",
            "## Summary",
            "",
            self.idea.summary,
            "",
            "## Source Metadata",
            "",
        ]

        if self.source_metadata:
            for key, value in self.source_metadata:
                lines.append(f"- {key}: {value}")
        else:
            lines.append("- None")

        lines.extend(
            [
                "",
                "## References",
                "",
            ]
        )

        if self.references:
            for reference in self.references:
                lines.extend(_reference_lines(reference))
        else:
            lines.append("- No references suggested.")

        if self.enrichment_note:
            lines.extend(["", "## Enrichment Note", "", self.enrichment_note])

        lines.extend(
            [
                "",
                "## Transcript Excerpt",
                "",
                f"> {self.transcript_excerpt}" if self.transcript_excerpt else "> (empty)",
            ]
        )
        return "\n".join(lines)


class MarkdownDraftTextRenderer:
    def render(self, draft: MarkdownDraft) -> str:
        return draft.to_markdown()


def build_excerpt(transcript: Transcript, limit: int = 36) -> str:
    words = transcript.text.split()
    excerpt = " ".join(words[:limit])
    if len(words) <= limit:
        return excerpt
    return f"{excerpt}..."


def _reference_lines(reference: ReferenceSuggestion) -> list[str]:
    lines = [f"- {reference.title}: {reference.support_note}"]
    if reference.url:
        lines.append(f"  - URL: {reference.url}")
    if reference.source_hint:
        lines.append(f"  - Source hint: {reference.source_hint}")
    return lines
