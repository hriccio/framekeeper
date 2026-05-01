from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_five_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/010-drafts-become-refined-pages.md",
        ROOT / "docs/episodes/011-review-before-publishing.md",
        ROOT / "docs/concepts/drafts-are-not-final.md",
        ROOT / "docs/concepts/review-preserves-context.md",
        ROOT / "docs/notes/0006-draft-to-refined-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_five_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Drafts Become Refined Pages](./episodes/010-drafts-become-refined-pages.md)" in index_text
    assert "[Review Before Publishing](./episodes/011-review-before-publishing.md)" in index_text
    assert "[Drafts Are Not Final](./concepts/drafts-are-not-final.md)" in index_text
    assert "[Review Preserves Context](./concepts/review-preserves-context.md)" in index_text
    assert "[Draft To Refined Workflow](./notes/0006-draft-to-refined-workflow.md)" in index_text


def test_section_indices_list_batch_five_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Drafts Become Refined Pages](./010-drafts-become-refined-pages.md)" in episodes_index
    assert "[Review Before Publishing](./011-review-before-publishing.md)" in episodes_index
    assert "[Drafts Are Not Final](./drafts-are-not-final.md)" in concepts_index
    assert "[Review Preserves Context](./review-preserves-context.md)" in concepts_index
    assert "[Draft To Refined Workflow](./0006-draft-to-refined-workflow.md)" in notes_index

