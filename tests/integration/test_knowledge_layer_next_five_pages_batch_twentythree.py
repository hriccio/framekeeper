from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentythree_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/046-packs-define-implementation-defaults.md",
        ROOT / "docs/episodes/047-python-ddd-monolith-is-a-selected-pack.md",
        ROOT / "docs/concepts/mrl-core-is-separate-from-packs.md",
        ROOT / "docs/concepts/runtime-topology-belongs-to-the-pack.md",
        ROOT / "docs/notes/0024-pack-selection-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentythree_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Packs Define Implementation Defaults](./episodes/046-packs-define-implementation-defaults.md)" in index_text
    assert "[Python DDD Monolith Is A Selected Pack](./episodes/047-python-ddd-monolith-is-a-selected-pack.md)" in index_text
    assert "[MRL Core Is Separate From Packs](./concepts/mrl-core-is-separate-from-packs.md)" in index_text
    assert "[Runtime Topology Belongs To The Pack](./concepts/runtime-topology-belongs-to-the-pack.md)" in index_text
    assert "[Pack Selection Workflow](./notes/0024-pack-selection-workflow.md)" in index_text


def test_section_indices_list_batch_twentythree_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Packs Define Implementation Defaults](./046-packs-define-implementation-defaults.md)" in episodes_index
    assert "[Python DDD Monolith Is A Selected Pack](./047-python-ddd-monolith-is-a-selected-pack.md)" in episodes_index
    assert "[MRL Core Is Separate From Packs](./mrl-core-is-separate-from-packs.md)" in concepts_index
    assert "[Runtime Topology Belongs To The Pack](./runtime-topology-belongs-to-the-pack.md)" in concepts_index
    assert "[Pack Selection Workflow](./0024-pack-selection-workflow.md)" in notes_index
