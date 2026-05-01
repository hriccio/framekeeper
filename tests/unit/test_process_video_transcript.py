from __future__ import annotations

from dataclasses import dataclass

from app.application.process_video_transcript import ProcessVideoTranscript
from app.domain.models import PacketStatus, RiskLevel, Transcript, VideoSubmission


@dataclass
class ExplodingSignalGenerator:
    def generate(self, transcript: Transcript):  # pragma: no cover - safety check
        raise AssertionError("signal generator should not run for blocked content")


def test_safe_transcript_reaches_ready_for_review_with_signal_feedback() -> None:
    processor = ProcessVideoTranscript()
    submission = VideoSubmission(
        video_id="video-001",
        title="Thinking about context",
        transcript=Transcript(
            "This episode is about how context changes the way we build software. "
            "I am keeping the example grounded in day to day work."
        ),
    )

    result = processor.execute(submission)

    assert result.safety_assessment.risk_level is RiskLevel.SAFE
    assert result.release_packet.status is PacketStatus.READY_FOR_REVIEW
    assert result.release_packet.ready_for_review is True
    assert result.signal_feedback is not None
    assert result.release_packet.signal_feedback is result.signal_feedback


def test_review_transcript_requires_manual_confirmation() -> None:
    processor = ProcessVideoTranscript()
    submission = VideoSubmission(
        video_id="video-002",
        transcript=Transcript(
            "This is not medical advice, but it does discuss a miracle cure and "
            "why people keep asking for guaranteed income."
        ),
    )

    result = processor.execute(submission)

    assert result.safety_assessment.risk_level is RiskLevel.REVIEW
    assert result.release_packet.status is PacketStatus.REQUIRES_MANUAL_CONFIRMATION
    assert result.release_packet.requires_manual_confirmation is True
    assert result.signal_feedback is not None


def test_blocked_transcript_skips_signal_feedback_and_blocks_packet() -> None:
    processor = ProcessVideoTranscript(signal_generator=ExplodingSignalGenerator())
    submission = VideoSubmission(
        video_id="video-003",
        transcript=Transcript(
            "This segment explains how to build a bomb and distribute malware."
        ),
    )

    result = processor.execute(submission)

    assert result.safety_assessment.risk_level is RiskLevel.BLOCK
    assert result.release_packet.status is PacketStatus.BLOCKED
    assert result.release_packet.blocked is True
    assert result.signal_feedback is None
    assert result.release_packet.signal_feedback is None
    assert "blocked content" in result.release_packet.to_markdown().lower()

