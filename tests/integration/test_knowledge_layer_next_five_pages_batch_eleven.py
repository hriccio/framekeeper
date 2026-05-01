from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_eleven_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/022-broken-links-are-regressions.md",
        ROOT / "docs/episodes/023-reading-paths-should-stay-obvious.md",
        ROOT / "docs/concepts/link-hygiene-keeps-the-site-trustworthy.md",
        ROOT / "docs/concepts/reading-path-is-part-of-editing.md",
        ROOT / "docs/notes/0012-link-checking-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_eleven_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Broken Links Are Regressions](./episodes/022-broken-links-are-regressions.md)" in index_text
    assert "[Reading Paths Should Stay Obvious](./episodes/023-reading-paths-should-stay-obvious.md)" in index_text
    assert "[Link Hygiene Keeps The Site Trustworthy](./concepts/link-hygiene-keeps-the-site-trustworthy.md)" in index_text
    assert "[Reading Path Is Part Of Editing](./concepts/reading-path-is-part-of-editing.md)" in index_text
    assert "[Link Checking Workflow](./notes/0012-link-checking-workflow.md)" in index_text


def test_section_indices_list_batch_eleven_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Broken Links Are Regressions](./022-broken-links-are-regressions.md)" in episodes_index
    assert "[Reading Paths Should Stay Obvious](./023-reading-paths-should-stay-obvious.md)" in episodes_index
    assert "[Link Hygiene Keeps The Site Trustworthy](./link-hygiene-keeps-the-site-trustworthy.md)" in concepts_index
    assert "[Reading Path Is Part Of Editing](./reading-path-is-part-of-editing.md)" in concepts_index
    assert "[Link Checking Workflow](./0012-link-checking-workflow.md)" in notes_index

