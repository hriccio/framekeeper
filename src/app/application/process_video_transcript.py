from __future__ import annotations

from dataclasses import dataclass

from app.domain.models import (
    PacketStatus,
    ReleasePacket,
    RiskLevel,
    SafetyAssessment,
    SignalFeedback,
    Transcript,
    VideoSubmission,
)
from app.domain.safety import TranscriptSafetyClassifier
from app.domain.signals import TranscriptSignalGenerator


@dataclass(frozen=True, slots=True)
class ProcessVideoTranscriptResult:
    submission: VideoSubmission
    safety_assessment: SafetyAssessment
    release_packet: ReleasePacket
    signal_feedback: SignalFeedback | None


class ProcessVideoTranscript:
    def __init__(
        self,
        safety_classifier: TranscriptSafetyClassifier | None = None,
        signal_generator: TranscriptSignalGenerator | None = None,
    ) -> None:
        self._safety_classifier = safety_classifier or TranscriptSafetyClassifier()
        self._signal_generator = signal_generator or TranscriptSignalGenerator()

    def execute(self, submission: VideoSubmission) -> ProcessVideoTranscriptResult:
        assessment = self._safety_classifier.classify(submission.transcript)

        if assessment.risk_level is RiskLevel.BLOCK:
            packet = self._build_packet(
                submission=submission,
                assessment=assessment,
                status=PacketStatus.BLOCKED,
                signal_feedback=None,
            )
            return ProcessVideoTranscriptResult(
                submission=submission,
                safety_assessment=assessment,
                release_packet=packet,
                signal_feedback=None,
            )

        signal_feedback = self._signal_generator.generate(submission.transcript)
        status = (
            PacketStatus.READY_FOR_REVIEW
            if assessment.risk_level is RiskLevel.SAFE
            else PacketStatus.REQUIRES_MANUAL_CONFIRMATION
        )
        packet = self._build_packet(
            submission=submission,
            assessment=assessment,
            status=status,
            signal_feedback=signal_feedback,
        )
        return ProcessVideoTranscriptResult(
            submission=submission,
            safety_assessment=assessment,
            release_packet=packet,
            signal_feedback=signal_feedback,
        )

    def _build_packet(
        self,
        submission: VideoSubmission,
        assessment: SafetyAssessment,
        status: PacketStatus,
        signal_feedback: SignalFeedback | None,
    ) -> ReleasePacket:
        excerpt = _excerpt(submission.transcript)
        return ReleasePacket(
            video_id=submission.video_id,
            title=submission.title,
            status=status,
            safety_assessment=assessment,
            transcript_excerpt=excerpt,
            signal_feedback=signal_feedback,
        )


def _excerpt(transcript: Transcript) -> str:
    words = transcript.text.split()
    excerpt = " ".join(words[:24])
    if len(words) <= 24:
        return excerpt
    return f"{excerpt}..."

