from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_twentyeight_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/056-transcript-fragments-need-an-editorial-angle.md",
        ROOT / "docs/episodes/057-source-rich-ideas-belong-in-references.md",
        ROOT / "docs/concepts/058-editorial-angle-guides-family-choice.md",
        ROOT / "docs/concepts/059-evidence-weight-shapes-content-form.md",
        ROOT / "docs/notes/0030-transcript-classification-checklist.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_twentyeight_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Transcript Fragments Need An Editorial Angle](./episodes/056-transcript-fragments-need-an-editorial-angle.md)" in index_text
    assert "[Source-Rich Ideas Belong In References](./episodes/057-source-rich-ideas-belong-in-references.md)" in index_text
    assert "[Editorial Angle Guides Family Choice](./concepts/058-editorial-angle-guides-family-choice.md)" in index_text
    assert "[Evidence Weight Shapes Content Form](./concepts/059-evidence-weight-shapes-content-form.md)" in index_text
    assert "[Transcript Classification Checklist](./notes/0030-transcript-classification-checklist.md)" in index_text


def test_section_indices_list_batch_twentyeight_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Transcript Fragments Need An Editorial Angle](./056-transcript-fragments-need-an-editorial-angle.md)" in episodes_index
    assert "[Source-Rich Ideas Belong In References](./057-source-rich-ideas-belong-in-references.md)" in episodes_index
    assert "[Editorial Angle Guides Family Choice](./058-editorial-angle-guides-family-choice.md)" in concepts_index
    assert "[Evidence Weight Shapes Content Form](./059-evidence-weight-shapes-content-form.md)" in concepts_index
    assert "[Transcript Classification Checklist](./0030-transcript-classification-checklist.md)" in notes_index
