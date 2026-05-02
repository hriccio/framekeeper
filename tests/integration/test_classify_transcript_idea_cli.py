from __future__ import annotations

from app.interfaces.cli.classify_transcript_idea import run


def test_classify_transcript_idea_cli_returns_family_summary() -> None:
    output = run(
        [
            "--video-id",
            "video-202",
            "--title",
            "Community guidelines and sources",
            "--transcript",
            "This walkthrough points to the official documentation and the community guidelines.",
        ]
    )

    assert "# Transcript Idea Classification" in output
    assert "- Video ID: video-202" in output
    assert "- Family: REFERENCE" in output
    assert "- Matched cue: community guidelines" in output
