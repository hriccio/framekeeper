from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Mapping


class RiskLevel(str, Enum):
    SAFE = "SAFE"
    REVIEW = "REVIEW"
    BLOCK = "BLOCK"


class PacketStatus(str, Enum):
    READY_FOR_REVIEW = "READY_FOR_REVIEW"
    REQUIRES_MANUAL_CONFIRMATION = "REQUIRES_MANUAL_CONFIRMATION"
    BLOCKED = "BLOCKED"


class ContentFamily(str, Enum):
    EPISODE = "EPISODE"
    CONCEPT = "CONCEPT"
    REFERENCE = "REFERENCE"
    NOTE = "NOTE"


@dataclass(frozen=True, slots=True)
class Transcript:
    text: str

    def __post_init__(self) -> None:
        normalized = self.text.strip()
        if not normalized:
            raise ValueError("transcript text cannot be empty")
        object.__setattr__(self, "text", normalized)


@dataclass(frozen=True, slots=True)
class VideoSubmission:
    video_id: str
    transcript: Transcript
    title: str | None = None
    metadata: Mapping[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        video_id = self.video_id.strip()
        if not video_id:
            raise ValueError("video_id cannot be empty")
        object.__setattr__(self, "video_id", video_id)
        if self.title is not None:
            title = self.title.strip()
            object.__setattr__(self, "title", title or None)


@dataclass(frozen=True, slots=True)
class SafetyAssessment:
    risk_level: RiskLevel
    reason: str


@dataclass(frozen=True, slots=True)
class SignalFeedback:
    summary: str
    audience: str
    hook: str
    clarity: int
    specificity: int
    coherence: int
    novelty: int


@dataclass(frozen=True, slots=True)
class ContentFamilyRecommendation:
    family: ContentFamily
    matched_cue: str
    reason: str


@dataclass(frozen=True, slots=True)
class ReleasePacket:
    video_id: str
    title: str | None
    status: PacketStatus
    safety_assessment: SafetyAssessment
    transcript_excerpt: str
    signal_feedback: SignalFeedback | None = None

    @property
    def ready_for_review(self) -> bool:
        return self.status is PacketStatus.READY_FOR_REVIEW

    @property
    def requires_manual_confirmation(self) -> bool:
        return self.status is PacketStatus.REQUIRES_MANUAL_CONFIRMATION

    @property
    def blocked(self) -> bool:
        return self.status is PacketStatus.BLOCKED

    def to_markdown(self) -> str:
        lines = [
            "# Release Packet",
            "",
            f"- Video ID: {self.video_id}",
            f"- Title: {self.title or '(untitled)'}",
            f"- Status: {self.status.value}",
            f"- Risk level: {self.safety_assessment.risk_level.value}",
            f"- Safety reason: {self.safety_assessment.reason}",
            f"- Transcript excerpt: {self.transcript_excerpt}",
        ]

        if self.signal_feedback is None:
            lines.extend(["", "## Signal Feedback", "", "Skipped for blocked content."])
            return "\n".join(lines)

        lines.extend(
            [
                "",
                "## Signal Feedback",
                "",
                f"- Summary: {self.signal_feedback.summary}",
                f"- Audience: {self.signal_feedback.audience}",
                f"- Hook: {self.signal_feedback.hook}",
                f"- Clarity: {self.signal_feedback.clarity}/10",
                f"- Specificity: {self.signal_feedback.specificity}/10",
                f"- Coherence: {self.signal_feedback.coherence}/10",
                f"- Novelty: {self.signal_feedback.novelty}/10",
            ]
        )
        return "\n".join(lines)
