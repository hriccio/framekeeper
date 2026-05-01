from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentyfive_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/050-release-decisions-stay-explicit.md",
        ROOT / "docs/episodes/051-exposure-follows-acceptance.md",
        ROOT / "docs/concepts/052-release-is-not-exposure.md",
        ROOT / "docs/concepts/053-portable-artifacts-support-exposure.md",
        ROOT / "docs/notes/0026-release-and-exposure-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentyfive_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Release Decisions Stay Explicit](./episodes/050-release-decisions-stay-explicit.md)" in index_text
    assert "[Exposure Follows Acceptance](./episodes/051-exposure-follows-acceptance.md)" in index_text
    assert "[Release Is Not Exposure](./concepts/052-release-is-not-exposure.md)" in index_text
    assert "[Portable Artifacts Support Exposure](./concepts/053-portable-artifacts-support-exposure.md)" in index_text
    assert "[Release And Exposure Workflow](./notes/0026-release-and-exposure-workflow.md)" in index_text


def test_section_indices_list_batch_twentyfive_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Release Decisions Stay Explicit](./050-release-decisions-stay-explicit.md)" in episodes_index
    assert "[Exposure Follows Acceptance](./051-exposure-follows-acceptance.md)" in episodes_index
    assert "[Release Is Not Exposure](./052-release-is-not-exposure.md)" in concepts_index
    assert "[Portable Artifacts Support Exposure](./053-portable-artifacts-support-exposure.md)" in concepts_index
    assert "[Release And Exposure Workflow](./0026-release-and-exposure-workflow.md)" in notes_index
