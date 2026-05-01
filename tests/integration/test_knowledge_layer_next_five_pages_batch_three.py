from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_three_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/006-references-support-episodes.md",
        ROOT / "docs/episodes/007-source-links-keep-episodes-honest.md",
        ROOT / "docs/concepts/curated-references-are-evidence.md",
        ROOT / "docs/references/youtube-community-guidelines.md",
        ROOT / "docs/notes/0004-reference-curation-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_three_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[References Support Episodes](./episodes/006-references-support-episodes.md)" in index_text
    assert "[Source Links Keep Episodes Honest](./episodes/007-source-links-keep-episodes-honest.md)" in index_text
    assert "[Curated References Are Evidence](./concepts/curated-references-are-evidence.md)" in index_text
    assert "[YouTube Community Guidelines](./references/youtube-community-guidelines.md)" in index_text
    assert "[Reference Curation Workflow](./notes/0004-reference-curation-workflow.md)" in index_text


def test_section_indices_list_batch_three_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    references_index = (ROOT / "docs/references/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[References Support Episodes](./006-references-support-episodes.md)" in episodes_index
    assert "[Source Links Keep Episodes Honest](./007-source-links-keep-episodes-honest.md)" in episodes_index
    assert "[Curated References Are Evidence](./curated-references-are-evidence.md)" in concepts_index
    assert "[YouTube Community Guidelines](./youtube-community-guidelines.md)" in references_index
    assert "[Reference Curation Workflow](./0004-reference-curation-workflow.md)" in notes_index

