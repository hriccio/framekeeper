from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_knowledge_layer_site_files_exist() -> None:
    expected_paths = [
        ROOT / "docs/index.md",
        ROOT / "docs/episodes/index.md",
        ROOT / "docs/concepts/index.md",
        ROOT / "docs/references/index.md",
        ROOT / "docs/episodes/001-template.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_docs_root_links_to_the_section_indices() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Episodes](./episodes/)" in index_text
    assert "[Concepts](./concepts/)" in index_text
    assert "[References](./references/)" in index_text

