from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_seven_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/014-older-pages-still-matter.md",
        ROOT / "docs/episodes/015-archives-are-readable.md",
        ROOT / "docs/concepts/version-history-is-visible.md",
        ROOT / "docs/concepts/archival-pages-stay-linked.md",
        ROOT / "docs/notes/0008-archive-maintenance-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_seven_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Older Pages Still Matter](./episodes/014-older-pages-still-matter.md)" in index_text
    assert "[Archives Are Readable](./episodes/015-archives-are-readable.md)" in index_text
    assert "[Version History Is Visible](./concepts/version-history-is-visible.md)" in index_text
    assert "[Archival Pages Stay Linked](./concepts/archival-pages-stay-linked.md)" in index_text
    assert "[Archive Maintenance Workflow](./notes/0008-archive-maintenance-workflow.md)" in index_text


def test_section_indices_list_batch_seven_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Older Pages Still Matter](./014-older-pages-still-matter.md)" in episodes_index
    assert "[Archives Are Readable](./015-archives-are-readable.md)" in episodes_index
    assert "[Version History Is Visible](./version-history-is-visible.md)" in concepts_index
    assert "[Archival Pages Stay Linked](./archival-pages-stay-linked.md)" in concepts_index
    assert "[Archive Maintenance Workflow](./0008-archive-maintenance-workflow.md)" in notes_index

