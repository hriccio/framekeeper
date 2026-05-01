from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentyseven_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/054-requests-need-clear-boundaries.md",
        ROOT / "docs/episodes/055-slice-maps-make-coverage-visible.md",
        ROOT / "docs/concepts/056-requests-are-review-units.md",
        ROOT / "docs/concepts/057-slice-docs-keep-build-bounded.md",
        ROOT / "docs/notes/0028-request-to-slice-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentyseven_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Requests Need Clear Boundaries](./episodes/054-requests-need-clear-boundaries.md)" in index_text
    assert "[Slice Maps Make Coverage Visible](./episodes/055-slice-maps-make-coverage-visible.md)" in index_text
    assert "[Requests Are Review Units](./concepts/056-requests-are-review-units.md)" in index_text
    assert "[Slice Docs Keep Build Bounded](./concepts/057-slice-docs-keep-build-bounded.md)" in index_text
    assert "[Request To Slice Workflow](./notes/0028-request-to-slice-workflow.md)" in index_text


def test_section_indices_list_batch_twentyseven_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Requests Need Clear Boundaries](./054-requests-need-clear-boundaries.md)" in episodes_index
    assert "[Slice Maps Make Coverage Visible](./055-slice-maps-make-coverage-visible.md)" in episodes_index
    assert "[Requests Are Review Units](./056-requests-are-review-units.md)" in concepts_index
    assert "[Slice Docs Keep Build Bounded](./057-slice-docs-keep-build-bounded.md)" in concepts_index
    assert "[Request To Slice Workflow](./0028-request-to-slice-workflow.md)" in notes_index
