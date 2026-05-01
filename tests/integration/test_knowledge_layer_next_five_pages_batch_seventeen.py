from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_seventeen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/034-overlapping-ideas-need-pruning.md",
        ROOT / "docs/episodes/035-pruned-pages-read-better.md",
        ROOT / "docs/concepts/overlap-hurts-the-page-family-model.md",
        ROOT / "docs/concepts/pruning-keeps-the-site-focused.md",
        ROOT / "docs/notes/0018-content-pruning-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_seventeen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Overlapping Ideas Need Pruning](./episodes/034-overlapping-ideas-need-pruning.md)" in index_text
    assert "[Pruned Pages Read Better](./episodes/035-pruned-pages-read-better.md)" in index_text
    assert "[Overlap Hurts The Page Family Model](./concepts/overlap-hurts-the-page-family-model.md)" in index_text
    assert "[Pruning Keeps The Site Focused](./concepts/pruning-keeps-the-site-focused.md)" in index_text
    assert "[Content Pruning Workflow](./notes/0018-content-pruning-workflow.md)" in index_text


def test_section_indices_list_batch_seventeen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Overlapping Ideas Need Pruning](./034-overlapping-ideas-need-pruning.md)" in episodes_index
    assert "[Pruned Pages Read Better](./035-pruned-pages-read-better.md)" in episodes_index
    assert "[Overlap Hurts The Page Family Model](./overlap-hurts-the-page-family-model.md)" in concepts_index
    assert "[Pruning Keeps The Site Focused](./pruning-keeps-the-site-focused.md)" in concepts_index
    assert "[Content Pruning Workflow](./0018-content-pruning-workflow.md)" in notes_index
