from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_batch_nine_knowledge_layer_pages_exist() -> None:
    expected_paths = [
        ROOT / "docs/episodes/018-titles-should-match-the-idea.md",
        ROOT / "docs/episodes/019-summaries-preserve-gist.md",
        ROOT / "docs/concepts/titles-and-summaries-have-different-jobs.md",
        ROOT / "docs/concepts/gist-should-stay-aligned.md",
        ROOT / "docs/notes/0010-title-summary-workflow.md",
    ]

    for path in expected_paths:
        assert path.exists(), path


def test_home_page_links_to_batch_nine_pages() -> None:
    index_text = (ROOT / "docs/index.md").read_text(encoding="utf-8")

    assert "[Titles Should Match The Idea](./episodes/018-titles-should-match-the-idea.md)" in index_text
    assert "[Summaries Preserve Gist](./episodes/019-summaries-preserve-gist.md)" in index_text
    assert "[Titles And Summaries Have Different Jobs](./concepts/titles-and-summaries-have-different-jobs.md)" in index_text
    assert "[Gist Should Stay Aligned](./concepts/gist-should-stay-aligned.md)" in index_text
    assert "[Title Summary Workflow](./notes/0010-title-summary-workflow.md)" in index_text


def test_section_indices_list_batch_nine_pages() -> None:
    episodes_index = (ROOT / "docs/episodes/index.md").read_text(encoding="utf-8")
    concepts_index = (ROOT / "docs/concepts/index.md").read_text(encoding="utf-8")
    notes_index = (ROOT / "docs/notes/index.md").read_text(encoding="utf-8")

    assert "[Titles Should Match The Idea](./018-titles-should-match-the-idea.md)" in episodes_index
    assert "[Summaries Preserve Gist](./019-summaries-preserve-gist.md)" in episodes_index
    assert "[Titles And Summaries Have Different Jobs](./titles-and-summaries-have-different-jobs.md)" in concepts_index
    assert "[Gist Should Stay Aligned](./gist-should-stay-aligned.md)" in concepts_index
    assert "[Title Summary Workflow](./0010-title-summary-workflow.md)" in notes_index

