from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_fourteen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/028-ideas-are-extracted-from-videos.md",
        ROOT / "docs/episodes/029-draft-pages-start-as-working-notes.md",
        ROOT / "docs/concepts/extraction-turns-transcripts-into-candidates.md",
        ROOT / "docs/concepts/draft-pages-need-editorial-shape.md",
        ROOT / "docs/notes/0015-idea-extraction-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_fourteen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Ideas Are Extracted From Videos](./episodes/028-ideas-are-extracted-from-videos.md)" in index_text
    assert "[Draft Pages Start As Working Notes](./episodes/029-draft-pages-start-as-working-notes.md)" in index_text
    assert "[Extraction Turns Transcripts Into Candidates](./concepts/extraction-turns-transcripts-into-candidates.md)" in index_text
    assert "[Draft Pages Need Editorial Shape](./concepts/draft-pages-need-editorial-shape.md)" in index_text
    assert "[Idea Extraction Workflow](./notes/0015-idea-extraction-workflow.md)" in index_text


def test_section_indices_list_batch_fourteen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Ideas Are Extracted From Videos](./028-ideas-are-extracted-from-videos.md)" in episodes_index
    assert "[Draft Pages Start As Working Notes](./029-draft-pages-start-as-working-notes.md)" in episodes_index
    assert "[Extraction Turns Transcripts Into Candidates](./extraction-turns-transcripts-into-candidates.md)" in concepts_index
    assert "[Draft Pages Need Editorial Shape](./draft-pages-need-editorial-shape.md)" in concepts_index
    assert "[Idea Extraction Workflow](./0015-idea-extraction-workflow.md)" in notes_index
