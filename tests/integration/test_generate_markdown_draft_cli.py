from __future__ import annotations

from app.application.generate_markdown_draft import GenerateMarkdownDraftResult
from app.domain.markdown_draft import (
    MarkdownDraft,
    ReferenceEnrichment,
    ReferenceSuggestion,
    TranscriptIdea,
)
from app.domain.models import ContentFamily, Transcript, VideoSubmission
from app.interfaces.cli.generate_markdown_draft import run


class FakeUseCase:
    def __init__(self) -> None:
        self.submission: VideoSubmission | None = None

    def execute(self, submission: VideoSubmission) -> GenerateMarkdownDraftResult:
        self.submission = submission
        idea = TranscriptIdea(
            title="Software development and AI",
            summary="A reflective transcript about software development with AI.",
            editorial_angle="AI is part of normal software development.",
            candidate_family=ContentFamily.EPISODE,
            rationale="The transcript is an episode-shaped reflection.",
        )
        enrichment = ReferenceEnrichment(
            references=(
                ReferenceSuggestion(
                    title="Ollama",
                    support_note="Local model runner for draft generation.",
                    source_hint="Installed on the machine",
                ),
            ),
            note="Fake use case output for CLI test.",
        )
        draft = MarkdownDraft(
            submission=submission,
            idea=idea,
            references=enrichment.references,
            transcript_excerpt=submission.transcript.text[:48],
            source_metadata=tuple(sorted(submission.metadata.items())),
            enrichment_note=enrichment.note,
        )
        return GenerateMarkdownDraftResult(
            submission=submission,
            idea=idea,
            reference_enrichment=enrichment,
            draft=draft,
            markdown=draft.to_markdown(),
        )


def test_generate_markdown_draft_cli_returns_markdown_from_use_case() -> None:
    use_case = FakeUseCase()
    output = run(
        [
            "--video-id",
            "video-202",
            "--title",
            "Community guidelines and sources",
            "--metadata",
            "speaker=Henrique",
            "--transcript",
            "This transcript becomes a markdown draft.",
        ],
        use_case=use_case,
    )

    assert use_case.submission is not None
    assert use_case.submission.video_id == "video-202"
    assert use_case.submission.title == "Community guidelines and sources"
    assert use_case.submission.metadata == {"speaker": "Henrique"}
    assert "# Markdown Draft" in output
    assert "AI is part of normal software development." in output
    assert "- speaker: Henrique" in output
