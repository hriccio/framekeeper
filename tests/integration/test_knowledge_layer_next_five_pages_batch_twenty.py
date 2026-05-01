from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twenty_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/040-videos-capture-thinking-in-motion.md",
        ROOT / "docs/episodes/041-refined-pages-preserve-the-idea.md",
        ROOT / "docs/concepts/exploratory-videos-need-extraction.md",
        ROOT / "docs/concepts/durable-pages-outlast-the-recording.md",
        ROOT / "docs/notes/0021-thinking-in-motion-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twenty_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Videos Capture Thinking In Motion](./episodes/040-videos-capture-thinking-in-motion.md)" in index_text
    assert "[Refined Pages Preserve The Idea](./episodes/041-refined-pages-preserve-the-idea.md)" in index_text
    assert "[Exploratory Videos Need Extraction](./concepts/exploratory-videos-need-extraction.md)" in index_text
    assert "[Durable Pages Outlast The Recording](./concepts/durable-pages-outlast-the-recording.md)" in index_text
    assert "[Thinking In Motion Workflow](./notes/0021-thinking-in-motion-workflow.md)" in index_text


def test_section_indices_list_batch_twenty_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Videos Capture Thinking In Motion](./040-videos-capture-thinking-in-motion.md)" in episodes_index
    assert "[Refined Pages Preserve The Idea](./041-refined-pages-preserve-the-idea.md)" in episodes_index
    assert "[Exploratory Videos Need Extraction](./exploratory-videos-need-extraction.md)" in concepts_index
    assert "[Durable Pages Outlast The Recording](./durable-pages-outlast-the-recording.md)" in concepts_index
    assert "[Thinking In Motion Workflow](./0021-thinking-in-motion-workflow.md)" in notes_index
