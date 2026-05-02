from __future__ import annotations

import argparse
from collections.abc import Sequence

from ...application.generate_markdown_draft import GenerateMarkdownDraft
from ...domain.models import Transcript, VideoSubmission
from ...infrastructure.ollama.markdown_draft_generation import (
    OllamaReferenceEnricher,
    OllamaTranscriptIdeaExtractor,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.app.interfaces.cli.generate_markdown_draft",
        description="Generate a markdown draft from a transcript.",
    )
    parser.add_argument("--video-id", required=True, help="Registered video identifier.")
    parser.add_argument(
        "--transcript",
        required=True,
        help="Transcript text to transform into a markdown draft.",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Optional video title.",
    )
    parser.add_argument(
        "--metadata",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="Optional metadata entries. Repeat to add more values.",
    )
    parser.add_argument(
        "--model",
        default="llama3",
        help="Ollama model name used for idea extraction and reference enrichment.",
    )
    parser.add_argument(
        "--timeout-seconds",
        type=float,
        default=60.0,
        help="Maximum time to wait for each Ollama call before falling back.",
    )
    return parser


def parse_metadata(entries: Sequence[str]) -> dict[str, str]:
    metadata: dict[str, str] = {}
    for entry in entries:
        if "=" not in entry:
            raise ValueError(f"invalid metadata entry: {entry!r}")
        key, value = entry.split("=", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"invalid metadata entry: {entry!r}")
        metadata[key] = value.strip()
    return metadata


def run(
    argv: Sequence[str] | None = None,
    use_case: GenerateMarkdownDraft | None = None,
) -> str:
    parser = build_parser()
    args = parser.parse_args(argv)
    metadata = parse_metadata(args.metadata)

    submission = VideoSubmission(
        video_id=args.video_id,
        title=args.title,
        transcript=Transcript(args.transcript),
        metadata=metadata,
    )
    service = use_case or GenerateMarkdownDraft(
        idea_extractor=OllamaTranscriptIdeaExtractor(
            model=args.model,
            timeout_seconds=args.timeout_seconds,
        ),
        reference_enricher=OllamaReferenceEnricher(
            model=args.model,
            timeout_seconds=args.timeout_seconds,
        ),
    )
    result = service.execute(submission)
    return result.markdown


def main(argv: Sequence[str] | None = None) -> int:
    print(run(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
