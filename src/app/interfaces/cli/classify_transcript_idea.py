from __future__ import annotations

import argparse
from collections.abc import Sequence

from ...application.classify_transcript_idea import ClassifyTranscriptIdea
from ...domain.models import Transcript, VideoSubmission


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.app.interfaces.cli.classify_transcript_idea",
        description="Classify a transcript-derived idea into a knowledge-layer family.",
    )
    parser.add_argument("--video-id", required=True, help="Registered video identifier.")
    parser.add_argument(
        "--transcript",
        required=True,
        help="Transcript text to classify.",
    )
    parser.add_argument(
        "--title",
        default=None,
        help="Optional video title.",
    )
    return parser


def run(argv: Sequence[str] | None = None) -> str:
    parser = build_parser()
    args = parser.parse_args(argv)

    submission = VideoSubmission(
        video_id=args.video_id,
        title=args.title,
        transcript=Transcript(args.transcript),
    )
    result = ClassifyTranscriptIdea().execute(submission)

    lines = [
        "# Transcript Idea Classification",
        "",
        f"- Video ID: {result.submission.video_id}",
        f"- Title: {result.submission.title or '(untitled)'}",
        f"- Family: {result.recommendation.family.value}",
        f"- Matched cue: {result.recommendation.matched_cue}",
        f"- Reason: {result.recommendation.reason}",
    ]
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    print(run(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
