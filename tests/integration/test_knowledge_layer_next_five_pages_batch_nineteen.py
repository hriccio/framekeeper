from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_nineteen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/038-review-is-not-block.md",
        ROOT / "docs/episodes/039-block-means-stop.md",
        ROOT / "docs/concepts/review-and-block-are-distinct.md",
        ROOT / "docs/concepts/overrides-stay-explicit.md",
        ROOT / "docs/notes/0020-safety-tier-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_nineteen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Review Is Not Block](./episodes/038-review-is-not-block.md)" in index_text
    assert "[Block Means Stop](./episodes/039-block-means-stop.md)" in index_text
    assert "[Review And Block Are Distinct](./concepts/review-and-block-are-distinct.md)" in index_text
    assert "[Overrides Stay Explicit](./concepts/overrides-stay-explicit.md)" in index_text
    assert "[Safety Tier Workflow](./notes/0020-safety-tier-workflow.md)" in index_text


def test_section_indices_list_batch_nineteen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Review Is Not Block](./038-review-is-not-block.md)" in episodes_index
    assert "[Block Means Stop](./039-block-means-stop.md)" in episodes_index
    assert "[Review And Block Are Distinct](./review-and-block-are-distinct.md)" in concepts_index
    assert "[Overrides Stay Explicit](./overrides-stay-explicit.md)" in concepts_index
    assert "[Safety Tier Workflow](./0020-safety-tier-workflow.md)" in notes_index
