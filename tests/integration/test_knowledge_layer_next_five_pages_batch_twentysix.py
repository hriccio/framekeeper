from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentysix_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/052-feedback-follows-exposure.md",
        ROOT / "docs/episodes/053-feedback-feeds-the-next-request.md",
        ROOT / "docs/concepts/054-feedback-is-distinct-from-signal.md",
        ROOT / "docs/concepts/055-feedback-reopens-the-loop.md",
        ROOT / "docs/notes/0027-feedback-capture-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentysix_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Feedback Follows Exposure](./episodes/052-feedback-follows-exposure.md)" in index_text
    assert "[Feedback Feeds The Next Request](./episodes/053-feedback-feeds-the-next-request.md)" in index_text
    assert "[Feedback Is Distinct From Signal](./concepts/054-feedback-is-distinct-from-signal.md)" in index_text
    assert "[Feedback Reopens The Loop](./concepts/055-feedback-reopens-the-loop.md)" in index_text
    assert "[Feedback Capture Workflow](./notes/0027-feedback-capture-workflow.md)" in index_text


def test_section_indices_list_batch_twentysix_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Feedback Follows Exposure](./052-feedback-follows-exposure.md)" in episodes_index
    assert "[Feedback Feeds The Next Request](./053-feedback-feeds-the-next-request.md)" in episodes_index
    assert "[Feedback Is Distinct From Signal](./054-feedback-is-distinct-from-signal.md)" in concepts_index
    assert "[Feedback Reopens The Loop](./055-feedback-reopens-the-loop.md)" in concepts_index
    assert "[Feedback Capture Workflow](./0027-feedback-capture-workflow.md)" in notes_index
