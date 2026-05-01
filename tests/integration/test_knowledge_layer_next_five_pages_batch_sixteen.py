from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_sixteen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/032-sources-need-refresh-cycles.md",
        ROOT / "docs/episodes/033-policy-references-age-over-time.md",
        ROOT / "docs/concepts/source-currency-keeps-trust-intact.md",
        ROOT / "docs/concepts/reference-drift-needs-review.md",
        ROOT / "docs/notes/0017-reference-refresh-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_sixteen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Sources Need Refresh Cycles](./episodes/032-sources-need-refresh-cycles.md)" in index_text
    assert "[Policy References Age Over Time](./episodes/033-policy-references-age-over-time.md)" in index_text
    assert "[Source Currency Keeps Trust Intact](./concepts/source-currency-keeps-trust-intact.md)" in index_text
    assert "[Reference Drift Needs Review](./concepts/reference-drift-needs-review.md)" in index_text
    assert "[Reference Refresh Workflow](./notes/0017-reference-refresh-workflow.md)" in index_text


def test_section_indices_list_batch_sixteen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Sources Need Refresh Cycles](./032-sources-need-refresh-cycles.md)" in episodes_index
    assert "[Policy References Age Over Time](./033-policy-references-age-over-time.md)" in episodes_index
    assert "[Source Currency Keeps Trust Intact](./source-currency-keeps-trust-intact.md)" in concepts_index
    assert "[Reference Drift Needs Review](./reference-drift-needs-review.md)" in concepts_index
    assert "[Reference Refresh Workflow](./0017-reference-refresh-workflow.md)" in notes_index
