from __future__ import annotations

from app.interfaces.cli.run_scenario import run


def test_run_scenario_cli_returns_markdown_release_packet() -> None:
    output = run(
        [
            "--video-id",
            "video-101",
            "--title",
            "Context and software",
            "--metadata",
            "speaker=Henrique",
            "--transcript",
            "This episode explains how context changes the way we build software.",
        ]
    )

    assert "# Release Packet" in output
    assert "- Video ID: video-101" in output
    assert "- Status: READY_FOR_REVIEW" in output
    assert "Signal Feedback" in output

