# Impact Analysis

- Change: `0018`
- Request: `work/changes/0018/request.md`
- Slice map: `work/changes/0018/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/028-ideas-are-extracted-from-videos.md`
- `docs/episodes/029-draft-pages-start-as-working-notes.md`
- `docs/concepts/extraction-turns-transcripts-into-candidates.md`
- `docs/concepts/draft-pages-need-editorial-shape.md`
- `docs/notes/0015-idea-extraction-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_fourteen.py`

## Impact Summary

This batch extends the knowledge layer with pages about extracting ideas and
shaping draft material.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- extraction turns raw transcript material into candidates
- drafts remain shaped but not yet final
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
