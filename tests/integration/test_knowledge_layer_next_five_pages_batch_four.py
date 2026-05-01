from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_four_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/008-episodes-should-stay-short.md",
        ROOT / "docs/episodes/009-concepts-point-to-episodes.md",
        ROOT / "docs/concepts/local-links-make-the-site-relatable.md",
        ROOT / "docs/concepts/source-discipline-keeps-content-honest.md",
        ROOT / "docs/notes/0005-adding-new-pages-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_four_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Episodes Should Stay Short](./episodes/008-episodes-should-stay-short.md)" in index_text
    assert "[Concepts Point To Episodes](./episodes/009-concepts-point-to-episodes.md)" in index_text
    assert "[Local Links Make The Site Relatable](./concepts/local-links-make-the-site-relatable.md)" in index_text
    assert "[Source Discipline Keeps Content Honest](./concepts/source-discipline-keeps-content-honest.md)" in index_text
    assert "[Adding New Pages Workflow](./notes/0005-adding-new-pages-workflow.md)" in index_text


def test_section_indices_list_batch_four_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Episodes Should Stay Short](./008-episodes-should-stay-short.md)" in episodes_index
    assert "[Concepts Point To Episodes](./009-concepts-point-to-episodes.md)" in episodes_index
    assert "[Local Links Make The Site Relatable](./local-links-make-the-site-relatable.md)" in concepts_index
    assert "[Source Discipline Keeps Content Honest](./source-discipline-keeps-content-honest.md)" in concepts_index
    assert "[Adding New Pages Workflow](./0005-adding-new-pages-workflow.md)" in notes_index

