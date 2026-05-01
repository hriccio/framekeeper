from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_next_five_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/002-automation-handles-mechanics.md",
        ROOT / "docs/episodes/003-safety-is-the-hard-gate.md",
        ROOT / "docs/concepts/human-final-authority.md",
        ROOT / "docs/concepts/safety-vs-signal.md",
        ROOT / "docs/notes/0002-raw-and-refined-routing.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_next_five_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Automation Handles Mechanics](./episodes/002-automation-handles-mechanics.md)" in index_text
    assert "[Safety Is The Hard Gate](./episodes/003-safety-is-the-hard-gate.md)" in index_text
    assert "[Human Final Authority](./concepts/human-final-authority.md)" in index_text
    assert "[Safety Vs Signal](./concepts/safety-vs-signal.md)" in index_text
    assert "[Raw And Refined Routing](./notes/0002-raw-and-refined-routing.md)" in index_text


def test_section_indices_list_next_five_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Automation Handles Mechanics](./002-automation-handles-mechanics.md)" in episodes_index
    assert "[Safety Is The Hard Gate](./003-safety-is-the-hard-gate.md)" in episodes_index
    assert "[Human Final Authority](./human-final-authority.md)" in concepts_index
    assert "[Safety Vs Signal](./safety-vs-signal.md)" in concepts_index
    assert "[Raw And Refined Routing](./0002-raw-and-refined-routing.md)" in notes_index

