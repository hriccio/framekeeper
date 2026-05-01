from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_six_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/012-metadata-keeps-pages-readable.md",
        ROOT / "docs/episodes/013-template-pages-prevent-drift.md",
        ROOT / "docs/concepts/page-shape-should-stay-predictable.md",
        ROOT / "docs/concepts/indices-are-part-of-the-content-model.md",
        ROOT / "docs/notes/0007-synchronizing-page-numbers.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_six_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Metadata Keeps Pages Readable](./episodes/012-metadata-keeps-pages-readable.md)" in index_text
    assert "[Template Pages Prevent Drift](./episodes/013-template-pages-prevent-drift.md)" in index_text
    assert "[Page Shape Should Stay Predictable](./concepts/page-shape-should-stay-predictable.md)" in index_text
    assert "[Indices Are Part Of The Content Model](./concepts/indices-are-part-of-the-content-model.md)" in index_text
    assert "[Synchronizing Page Numbers](./notes/0007-synchronizing-page-numbers.md)" in index_text


def test_section_indices_list_batch_six_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Metadata Keeps Pages Readable](./012-metadata-keeps-pages-readable.md)" in episodes_index
    assert "[Template Pages Prevent Drift](./013-template-pages-prevent-drift.md)" in episodes_index
    assert "[Page Shape Should Stay Predictable](./page-shape-should-stay-predictable.md)" in concepts_index
    assert "[Indices Are Part Of The Content Model](./indices-are-part-of-the-content-model.md)" in concepts_index
    assert "[Synchronizing Page Numbers](./0007-synchronizing-page-numbers.md)" in notes_index

