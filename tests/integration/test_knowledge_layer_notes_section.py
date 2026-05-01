from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_knowledge_layer_notes_files_exist() -> None:
    expected_paths = [
        ROOT / "docs/notes/index.md",
        ROOT / "docs/notes/0001-working-notes.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_notes_section() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Working Notes](./notes/0001-working-notes.md)" in index_text


def test_notes_index_links_to_seeded_note() -> None:
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Working Notes](./0001-working-notes.md)" in notes_index

