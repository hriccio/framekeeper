from __future__ import annotations

from dataclasses import dataclass

from ..domain.markdown_draft import (
    MarkdownDraft,
    MarkdownDraftTextRenderer,
    ReferenceEnrichment,
    TranscriptIdea,
    build_excerpt,
)
from ..domain.models import VideoSubmission
from .ports.markdown_draft_generation import (
    MarkdownDraftRenderer,
    ReferenceEnricher,
    TranscriptIdeaExtractor,
)


@dataclass(frozen=True, slots=True)
class GenerateMarkdownDraftResult:
    submission: VideoSubmission
    idea: TranscriptIdea
    reference_enrichment: ReferenceEnrichment
    draft: MarkdownDraft
    markdown: str


class GenerateMarkdownDraft:
    def __init__(
        self,
        idea_extractor: TranscriptIdeaExtractor,
        reference_enricher: ReferenceEnricher,
        renderer: MarkdownDraftRenderer | None = None,
    ) -> None:
        self._idea_extractor = idea_extractor
        self._reference_enricher = reference_enricher
        self._renderer = renderer or MarkdownDraftTextRenderer()

    def execute(self, submission: VideoSubmission) -> GenerateMarkdownDraftResult:
        idea = self._idea_extractor.extract(submission)
        reference_enrichment = self._reference_enricher.enrich(submission, idea)
        draft = MarkdownDraft(
            submission=submission,
            idea=idea,
            references=reference_enrichment.references,
            transcript_excerpt=build_excerpt(submission.transcript),
            source_metadata=tuple(sorted(submission.metadata.items())),
            enrichment_note=reference_enrichment.note,
        )
        markdown = self._renderer.render(draft)
        return GenerateMarkdownDraftResult(
            submission=submission,
            idea=idea,
            reference_enrichment=reference_enrichment,
            draft=draft,
            markdown=markdown,
        )
