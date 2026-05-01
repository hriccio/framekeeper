from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentyfour_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/048-scenario-evaluation-is-not-tests.md",
        ROOT / "docs/episodes/049-lightweight-egd-is-the-earlier-stage-default.md",
        ROOT / "docs/concepts/050-validation-modes-guide-slice-strategy.md",
        ROOT / "docs/concepts/051-deterministic-packets-keep-evidence-reviewable.md",
        ROOT / "docs/notes/0025-scenario-evaluation-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentyfour_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Scenario Evaluation Is Not Tests](./episodes/048-scenario-evaluation-is-not-tests.md)" in index_text
    assert "[Lightweight EGD Is The Earlier-Stage Default](./episodes/049-lightweight-egd-is-the-earlier-stage-default.md)" in index_text
    assert "[Validation Modes Guide Slice Strategy](./concepts/050-validation-modes-guide-slice-strategy.md)" in index_text
    assert "[Deterministic Packets Keep Evidence Reviewable](./concepts/051-deterministic-packets-keep-evidence-reviewable.md)" in index_text
    assert "[Scenario Evaluation Workflow](./notes/0025-scenario-evaluation-workflow.md)" in index_text


def test_section_indices_list_batch_twentyfour_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Scenario Evaluation Is Not Tests](./048-scenario-evaluation-is-not-tests.md)" in episodes_index
    assert "[Lightweight EGD Is The Earlier-Stage Default](./049-lightweight-egd-is-the-earlier-stage-default.md)" in episodes_index
    assert "[Validation Modes Guide Slice Strategy](./050-validation-modes-guide-slice-strategy.md)" in concepts_index
    assert "[Deterministic Packets Keep Evidence Reviewable](./051-deterministic-packets-keep-evidence-reviewable.md)" in concepts_index
    assert "[Scenario Evaluation Workflow](./0025-scenario-evaluation-workflow.md)" in notes_index
