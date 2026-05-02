from __future__ import annotations

from dataclasses import dataclass

from ..domain.content_classification import (
    ContentFamilyRecommendation,
    TranscriptIdeaClassifier,
)
from ..domain.models import VideoSubmission


@dataclass(frozen=True, slots=True)
class ClassifyTranscriptIdeaResult:
    submission: VideoSubmission
    recommendation: ContentFamilyRecommendation


class ClassifyTranscriptIdea:
    def __init__(
        self,
        classifier: TranscriptIdeaClassifier | None = None,
    ) -> None:
        self._classifier = classifier or TranscriptIdeaClassifier()

    def execute(self, submission: VideoSubmission) -> ClassifyTranscriptIdeaResult:
        recommendation = self._classifier.classify(submission)
        return ClassifyTranscriptIdeaResult(
            submission=submission,
            recommendation=recommendation,
        )
