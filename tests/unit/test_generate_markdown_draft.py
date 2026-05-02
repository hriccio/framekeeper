from __future__ import annotations

from app.application.generate_markdown_draft import GenerateMarkdownDraft
from app.domain.markdown_draft import (
    MarkdownDraft,
    ReferenceEnrichment,
    ReferenceSuggestion,
    TranscriptIdea,
)
from app.domain.models import ContentFamily, Transcript, VideoSubmission


def test_generate_markdown_draft_runs_extraction_before_enrichment_and_rendering() -> None:
    calls: list[str] = []

    class FakeIdeaExtractor:
        def extract(self, submission: VideoSubmission) -> TranscriptIdea:
            calls.append("extract")
            assert submission.video_id == "video-001"
            return TranscriptIdea(
                title="AI changes software work",
                summary="The transcript reflects on AI as normal software tooling.",
                editorial_angle="AI is now part of normal development practice.",
                candidate_family=ContentFamily.EPISODE,
                rationale="Reflective and narrative content fits the episode family.",
            )

    class FakeReferenceEnricher:
        def enrich(
            self,
            submission: VideoSubmission,
            idea: TranscriptIdea,
        ) -> ReferenceEnrichment:
            calls.append("enrich")
            assert submission.video_id == "video-001"
            assert idea.title == "AI changes software work"
            return ReferenceEnrichment(
                references=(
                    ReferenceSuggestion(
                        title="Ollama",
                        support_note="Local model runtime used by the draft flow.",
                        source_hint="Local CLI installation",
                    ),
                ),
                note="Reference enrichment is intentionally lightweight here.",
            )

    class FakeRenderer:
        def render(self, draft: MarkdownDraft) -> str:
            calls.append("render")
            assert draft.idea.editorial_angle == "AI is now part of normal development practice."
            return draft.to_markdown()

    result = GenerateMarkdownDraft(
        idea_extractor=FakeIdeaExtractor(),
        reference_enricher=FakeReferenceEnricher(),
        renderer=FakeRenderer(),
    ).execute(
        VideoSubmission(
            video_id="video-001",
            title="Thinking about software development",
            transcript=Transcript(
                "This is a transcript about how AI is changing software development."
            ),
            metadata={"speaker": "Henrique"},
        )
    )

    assert calls == ["extract", "enrich", "render"]
    assert result.submission.video_id == "video-001"
    assert result.draft.references[0].title == "Ollama"
    assert "# Markdown Draft" in result.markdown
    assert "- Candidate family: EPISODE" in result.markdown
    assert "- speaker: Henrique" in result.markdown
    assert "Reference enrichment is intentionally lightweight here." in result.markdown
