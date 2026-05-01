from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_knowledge_layer_content_seed_files_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/001-contexto-em-ia.md",
        ROOT / "docs/concepts/contexto-em-ia.md",
        ROOT / "docs/references/github-pages.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_seeded_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Contexto Em IA episode](./episodes/001-contexto-em-ia.md)" in index_text
    assert "[Contexto Em IA concept](./concepts/contexto-em-ia.md)" in index_text
    assert "[GitHub Pages reference](./references/github-pages.md)" in index_text


def test_section_indices_list_seeded_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    references_index = (ROOT / "docs/references/index.md").read_text(encoding="utf-8")

    assert "[Contexto Em IA](./001-contexto-em-ia.md)" in episodes_index
    assert "[Contexto Em IA](./contexto-em-ia.md)" in concepts_index
    assert "[GitHub Pages](./github-pages.md)" in references_index

