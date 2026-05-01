from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentyone_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/042-work-sources-hold-raw-evidence.md",
        ROOT / "docs/episodes/043-work-changes-preserve-loop-history.md",
        ROOT / "docs/concepts/memory-is-split-by-purpose.md",
        ROOT / "docs/concepts/change-artifacts-keep-the-loop-readable.md",
        ROOT / "docs/notes/0022-repository-memory-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentyone_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Work Sources Hold Raw Evidence](./episodes/042-work-sources-hold-raw-evidence.md)" in index_text
    assert "[Work Changes Preserve Loop History](./episodes/043-work-changes-preserve-loop-history.md)" in index_text
    assert "[Memory Is Split By Purpose](./concepts/memory-is-split-by-purpose.md)" in index_text
    assert "[Change Artifacts Keep The Loop Readable](./concepts/change-artifacts-keep-the-loop-readable.md)" in index_text
    assert "[Repository Memory Workflow](./notes/0022-repository-memory-workflow.md)" in index_text


def test_section_indices_list_batch_twentyone_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Work Sources Hold Raw Evidence](./042-work-sources-hold-raw-evidence.md)" in episodes_index
    assert "[Work Changes Preserve Loop History](./043-work-changes-preserve-loop-history.md)" in episodes_index
    assert "[Memory Is Split By Purpose](./memory-is-split-by-purpose.md)" in concepts_index
    assert "[Change Artifacts Keep The Loop Readable](./change-artifacts-keep-the-loop-readable.md)" in concepts_index
    assert "[Repository Memory Workflow](./0022-repository-memory-workflow.md)" in notes_index
