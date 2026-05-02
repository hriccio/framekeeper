from __future__ import annotations

from typing import Protocol

from ...domain.markdown_draft import (
    MarkdownDraft,
    ReferenceEnrichment,
    TranscriptIdea,
)
from ...domain.models import VideoSubmission


class TranscriptIdeaExtractor(Protocol):
    def extract(self, submission: VideoSubmission) -> TranscriptIdea:
        ...


class ReferenceEnricher(Protocol):
    def enrich(
        self,
        submission: VideoSubmission,
        idea: TranscriptIdea,
    ) -> ReferenceEnrichment:
        ...


class MarkdownDraftRenderer(Protocol):
    def render(self, draft: MarkdownDraft) -> str:
        ...
