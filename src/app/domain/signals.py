from __future__ import annotations

from collections import Counter
import re

from .models import SignalFeedback, Transcript

STOP_WORDS = {
    "a",
    "and",
    "as",
    "be",
    "for",
    "from",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "the",
    "this",
    "to",
    "with",
}


class TranscriptSignalGenerator:
    def generate(self, transcript: Transcript) -> SignalFeedback:
        words = _words(transcript.text)
        content_words = [word for word in words if word not in STOP_WORDS]
        top_terms = [term for term, _ in Counter(content_words).most_common(3)]

        subject = ", ".join(top_terms) if top_terms else "the topic"
        summary = _sentence_or_excerpt(transcript.text)
        audience = f"People interested in {subject}."
        hook = f"It offers a direct look at {subject}."

        word_count = len(words)
        sentence_count = max(1, transcript.text.count(".") + transcript.text.count("!") + transcript.text.count("?"))
        diversity = len(set(content_words))

        clarity = min(10, 4 + sentence_count + word_count // 60)
        specificity = min(10, 3 + diversity // 5)
        coherence = min(10, 4 + sentence_count)
        novelty = min(10, 2 + diversity // 8)

        return SignalFeedback(
            summary=summary,
            audience=audience,
            hook=hook,
            clarity=clarity,
            specificity=specificity,
            coherence=coherence,
            novelty=novelty,
        )


def _words(text: str) -> list[str]:
    return re.findall(r"[a-z0-9']+", text.lower())


def _sentence_or_excerpt(text: str) -> str:
    parts = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)
    if parts and parts[0]:
        return parts[0]

    words = text.split()
    excerpt = " ".join(words[:18])
    return excerpt if len(words) <= 18 else f"{excerpt}..."

