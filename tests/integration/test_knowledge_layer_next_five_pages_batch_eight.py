from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_eight_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/016-content-families-keep-the-site-structured.md",
        ROOT / "docs/episodes/017-notes-are-for-intermediate-thinking.md",
        ROOT / "docs/concepts/page-families-have-different-jobs.md",
        ROOT / "docs/concepts/reference-pages-need-scope.md",
        ROOT / "docs/notes/0009-page-family-map.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_eight_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Content Families Keep The Site Structured](./episodes/016-content-families-keep-the-site-structured.md)" in index_text
    assert "[Notes Are For Intermediate Thinking](./episodes/017-notes-are-for-intermediate-thinking.md)" in index_text
    assert "[Page Families Have Different Jobs](./concepts/page-families-have-different-jobs.md)" in index_text
    assert "[Reference Pages Need Scope](./concepts/reference-pages-need-scope.md)" in index_text
    assert "[Page Family Map](./notes/0009-page-family-map.md)" in index_text


def test_section_indices_list_batch_eight_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Content Families Keep The Site Structured](./016-content-families-keep-the-site-structured.md)" in episodes_index
    assert "[Notes Are For Intermediate Thinking](./017-notes-are-for-intermediate-thinking.md)" in episodes_index
    assert "[Page Families Have Different Jobs](./page-families-have-different-jobs.md)" in concepts_index
    assert "[Reference Pages Need Scope](./reference-pages-need-scope.md)" in concepts_index
    assert "[Page Family Map](./0009-page-family-map.md)" in notes_index

