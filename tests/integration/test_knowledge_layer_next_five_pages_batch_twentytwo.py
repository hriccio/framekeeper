from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentytwo_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/044-processing-runs-stay-inspectable.md",
        ROOT / "docs/episodes/045-transcripts-and-metadata-travel-together.md",
        ROOT / "docs/concepts/inspectable-runs-need-clear-artifacts.md",
        ROOT / "docs/concepts/transcripts-are-intermediate-artifacts.md",
        ROOT / "docs/notes/0023-processing-run-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentytwo_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Processing Runs Stay Inspectable](./episodes/044-processing-runs-stay-inspectable.md)" in index_text
    assert "[Transcripts And Metadata Travel Together](./episodes/045-transcripts-and-metadata-travel-together.md)" in index_text
    assert "[Inspectable Runs Need Clear Artifacts](./concepts/inspectable-runs-need-clear-artifacts.md)" in index_text
    assert "[Transcripts Are Intermediate Artifacts](./concepts/transcripts-are-intermediate-artifacts.md)" in index_text
    assert "[Processing Run Workflow](./notes/0023-processing-run-workflow.md)" in index_text


def test_section_indices_list_batch_twentytwo_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Processing Runs Stay Inspectable](./044-processing-runs-stay-inspectable.md)" in episodes_index
    assert "[Transcripts And Metadata Travel Together](./045-transcripts-and-metadata-travel-together.md)" in episodes_index
    assert "[Inspectable Runs Need Clear Artifacts](./inspectable-runs-need-clear-artifacts.md)" in concepts_index
    assert "[Transcripts Are Intermediate Artifacts](./transcripts-are-intermediate-artifacts.md)" in concepts_index
    assert "[Processing Run Workflow](./0023-processing-run-workflow.md)" in notes_index
