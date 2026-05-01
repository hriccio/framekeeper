from __future__ import annotations

from dataclasses import dataclass

from .models import RiskLevel, SafetyAssessment, Transcript

BLOCK_PATTERNS: tuple[tuple[str, str], ...] = (
    ("how to build a bomb", "dangerous instructions"),
    ("phishing", "phishing or scam content"),
    ("copyright infringement", "copyright violation"),
    ("hate speech", "hate speech"),
    ("malware", "malware distribution"),
    ("scam", "scam or deceptive practices"),
)

REVIEW_PATTERNS: tuple[tuple[str, str], ...] = (
    ("guaranteed income", "claims about guaranteed income"),
    ("make money fast", "financial hype"),
    ("medical advice", "medical advice"),
    ("miracle cure", "unverified health claims"),
    ("hack", "potentially risky technical instructions"),
)


@dataclass(slots=True)
class TranscriptSafetyClassifier:
    def classify(self, transcript: Transcript) -> SafetyAssessment:
        normalized = _normalize(transcript.text)

        for pattern, reason in BLOCK_PATTERNS:
            if pattern in normalized:
                return SafetyAssessment(risk_level=RiskLevel.BLOCK, reason=reason)

        for pattern, reason in REVIEW_PATTERNS:
            if pattern in normalized:
                return SafetyAssessment(risk_level=RiskLevel.REVIEW, reason=reason)

        return SafetyAssessment(
            risk_level=RiskLevel.SAFE,
            reason="no high-risk indicators detected",
        )


def _normalize(text: str) -> str:
    return " ".join(text.lower().split())

