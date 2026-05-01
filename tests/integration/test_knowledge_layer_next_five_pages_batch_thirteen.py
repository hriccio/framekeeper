from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_thirteen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/026-raw-transcripts-stay-private.md",
        ROOT / "docs/episodes/027-public-pages-are-refined.md",
        ROOT / "docs/concepts/raw-evidence-is-not-the-site.md",
        ROOT / "docs/concepts/public-content-needs-selection.md",
        ROOT / "docs/notes/0014-transcript-to-public-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_thirteen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Raw Transcripts Stay Private](./episodes/026-raw-transcripts-stay-private.md)" in index_text
    assert "[Public Pages Are Refined](./episodes/027-public-pages-are-refined.md)" in index_text
    assert "[Raw Evidence Is Not The Site](./concepts/raw-evidence-is-not-the-site.md)" in index_text
    assert "[Public Content Needs Selection](./concepts/public-content-needs-selection.md)" in index_text
    assert "[Transcript To Public Workflow](./notes/0014-transcript-to-public-workflow.md)" in index_text


def test_section_indices_list_batch_thirteen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Raw Transcripts Stay Private](./026-raw-transcripts-stay-private.md)" in episodes_index
    assert "[Public Pages Are Refined](./027-public-pages-are-refined.md)" in episodes_index
    assert "[Raw Evidence Is Not The Site](./raw-evidence-is-not-the-site.md)" in concepts_index
    assert "[Public Content Needs Selection](./public-content-needs-selection.md)" in concepts_index
    assert "[Transcript To Public Workflow](./0014-transcript-to-public-workflow.md)" in notes_index
