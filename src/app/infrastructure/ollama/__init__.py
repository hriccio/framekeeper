"""Ollama-backed adapters for Framekeeper."""

from .markdown_draft_generation import (
    OllamaReferenceEnricher,
    OllamaTranscriptIdeaExtractor,
)

__all__ = [
    "OllamaReferenceEnricher",
    "OllamaTranscriptIdeaExtractor",
]
