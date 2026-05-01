from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_eighteen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/036-signal-feedback-stays-diagnostic.md",
        ROOT / "docs/episodes/037-release-packets-support-review.md",
        ROOT / "docs/concepts/signal-is-not-the-release-gate.md",
        ROOT / "docs/concepts/release-packets-keep-review-explicit.md",
        ROOT / "docs/notes/0019-signal-to-release-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_eighteen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Signal Feedback Stays Diagnostic](./episodes/036-signal-feedback-stays-diagnostic.md)" in index_text
    assert "[Release Packets Support Review](./episodes/037-release-packets-support-review.md)" in index_text
    assert "[Signal Is Not The Release Gate](./concepts/signal-is-not-the-release-gate.md)" in index_text
    assert "[Release Packets Keep Review Explicit](./concepts/release-packets-keep-review-explicit.md)" in index_text
    assert "[Signal To Release Workflow](./notes/0019-signal-to-release-workflow.md)" in index_text


def test_section_indices_list_batch_eighteen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Signal Feedback Stays Diagnostic](./036-signal-feedback-stays-diagnostic.md)" in episodes_index
    assert "[Release Packets Support Review](./037-release-packets-support-review.md)" in episodes_index
    assert "[Signal Is Not The Release Gate](./signal-is-not-the-release-gate.md)" in concepts_index
    assert "[Release Packets Keep Review Explicit](./release-packets-keep-review-explicit.md)" in concepts_index
    assert "[Signal To Release Workflow](./0019-signal-to-release-workflow.md)" in notes_index
