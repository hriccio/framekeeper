from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_fifteen_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/030-candidate-ideas-need-a-family.md",
        ROOT / "docs/episodes/031-references-become-reference-pages.md",
        ROOT / "docs/concepts/family-assignment-keeps-drafts-clear.md",
        ROOT / "docs/concepts/draft-candidates-need-a-destination.md",
        ROOT / "docs/notes/0016-candidate-promotion-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_fifteen_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Candidate Ideas Need A Family](./episodes/030-candidate-ideas-need-a-family.md)" in index_text
    assert "[References Become Reference Pages](./episodes/031-references-become-reference-pages.md)" in index_text
    assert "[Family Assignment Keeps Drafts Clear](./concepts/family-assignment-keeps-drafts-clear.md)" in index_text
    assert "[Draft Candidates Need A Destination](./concepts/draft-candidates-need-a-destination.md)" in index_text
    assert "[Candidate Promotion Workflow](./notes/0016-candidate-promotion-workflow.md)" in index_text


def test_section_indices_list_batch_fifteen_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Candidate Ideas Need A Family](./030-candidate-ideas-need-a-family.md)" in episodes_index
    assert "[References Become Reference Pages](./031-references-become-reference-pages.md)" in episodes_index
    assert "[Family Assignment Keeps Drafts Clear](./family-assignment-keeps-drafts-clear.md)" in concepts_index
    assert "[Draft Candidates Need A Destination](./draft-candidates-need-a-destination.md)" in concepts_index
    assert "[Candidate Promotion Workflow](./0016-candidate-promotion-workflow.md)" in notes_index
