from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_two_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/004-markdown-is-the-source-of-truth.md",
        ROOT / "docs/episodes/005-github-pages-is-enough-for-now.md",
        ROOT / "docs/concepts/wnt-and-codingzen-stay-separate.md",
        ROOT / "docs/concepts/manual-publishing-rhythm.md",
        ROOT / "docs/notes/0003-published-content-is-not-raw-evidence.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_two_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Markdown Is The Source Of Truth](./episodes/004-markdown-is-the-source-of-truth.md)" in index_text
    assert "[GitHub Pages Is Enough For Now](./episodes/005-github-pages-is-enough-for-now.md)" in index_text
    assert "[WNT And CodingZen Stay Separate](./concepts/wnt-and-codingzen-stay-separate.md)" in index_text
    assert "[Manual Publishing Rhythm](./concepts/manual-publishing-rhythm.md)" in index_text
    assert "[Published Content Is Not Raw Evidence](./notes/0003-published-content-is-not-raw-evidence.md)" in index_text


def test_section_indices_list_batch_two_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Markdown Is The Source Of Truth](./004-markdown-is-the-source-of-truth.md)" in episodes_index
    assert "[GitHub Pages Is Enough For Now](./005-github-pages-is-enough-for-now.md)" in episodes_index
    assert "[WNT And CodingZen Stay Separate](./wnt-and-codingzen-stay-separate.md)" in concepts_index
    assert "[Manual Publishing Rhythm](./manual-publishing-rhythm.md)" in concepts_index
    assert "[Published Content Is Not Raw Evidence](./0003-published-content-is-not-raw-evidence.md)" in notes_index

