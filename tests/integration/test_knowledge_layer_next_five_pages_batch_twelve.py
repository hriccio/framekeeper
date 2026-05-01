from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twelve_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/024-references-should-stay-targeted.md",
        ROOT / "docs/episodes/025-source-links-need-an-anchor.md",
        ROOT / "docs/concepts/claims-and-sources-stay-paired.md",
        ROOT / "docs/concepts/reference-pages-are-not-dumps.md",
        ROOT / "docs/notes/0013-reference-review-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twelve_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[References Should Stay Targeted](./episodes/024-references-should-stay-targeted.md)" in index_text
    assert "[Source Links Need An Anchor](./episodes/025-source-links-need-an-anchor.md)" in index_text
    assert "[Claims And Sources Stay Paired](./concepts/claims-and-sources-stay-paired.md)" in index_text
    assert "[Reference Pages Are Not Dumps](./concepts/reference-pages-are-not-dumps.md)" in index_text
    assert "[Reference Review Workflow](./notes/0013-reference-review-workflow.md)" in index_text


def test_section_indices_list_batch_twelve_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[References Should Stay Targeted](./024-references-should-stay-targeted.md)" in episodes_index
    assert "[Source Links Need An Anchor](./025-source-links-need-an-anchor.md)" in episodes_index
    assert "[Claims And Sources Stay Paired](./claims-and-sources-stay-paired.md)" in concepts_index
    assert "[Reference Pages Are Not Dumps](./reference-pages-are-not-dumps.md)" in concepts_index
    assert "[Reference Review Workflow](./0013-reference-review-workflow.md)" in notes_index
