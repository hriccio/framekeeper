from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_ten_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/020-home-page-is-a-curated-entry-point.md",
        ROOT / "docs/episodes/021-featured-links-should-stay-selective.md",
        ROOT / "docs/concepts/curated-entry-points-reduce-friction.md",
        ROOT / "docs/concepts/home-pages-should-favor-signal.md",
        ROOT / "docs/notes/0011-front-door-curation-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_ten_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Home Page Is A Curated Entry Point](./episodes/020-home-page-is-a-curated-entry-point.md)" in index_text
    assert "[Featured Links Should Stay Selective](./episodes/021-featured-links-should-stay-selective.md)" in index_text
    assert "[Curated Entry Points Reduce Friction](./concepts/curated-entry-points-reduce-friction.md)" in index_text
    assert "[Home Pages Should Favor Signal](./concepts/home-pages-should-favor-signal.md)" in index_text
    assert "[Front Door Curation Workflow](./notes/0011-front-door-curation-workflow.md)" in index_text


def test_section_indices_list_batch_ten_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Home Page Is A Curated Entry Point](./020-home-page-is-a-curated-entry-point.md)" in episodes_index
    assert "[Featured Links Should Stay Selective](./021-featured-links-should-stay-selective.md)" in episodes_index
    assert "[Curated Entry Points Reduce Friction](./curated-entry-points-reduce-friction.md)" in concepts_index
    assert "[Home Pages Should Favor Signal](./home-pages-should-favor-signal.md)" in concepts_index
    assert "[Front Door Curation Workflow](./0011-front-door-curation-workflow.md)" in notes_index

