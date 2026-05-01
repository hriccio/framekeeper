from __future__ import annotations

import argparse
from collections.abc import Sequence
from typing import Mapping

from ...application.process_video_transcript import ProcessVideoTranscript
from ...domain.models import Transcript, VideoSubmission


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m src.app.interfaces.cli.run_scenario",
        description="Run the Framekeeper transcript classification scenario.",
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
    parser.add_argument(
        "--metadata",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="Optional metadata entries. Repeat to add more values.",
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


def run(argv: Sequence[str] | None = None) -> str:
    parser = build_parser()
    args = parser.parse_args(argv)
    metadata = parse_metadata(args.metadata)

    submission = VideoSubmission(
        video_id=args.video_id,
        title=args.title,
        transcript=Transcript(args.transcript),
        metadata=metadata,
    )
    result = ProcessVideoTranscript().execute(submission)
    return result.release_packet.to_markdown()


def main(argv: Sequence[str] | None = None) -> int:
    print(run(argv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
