# Impact Analysis

- Change: `0021`
- Request: `work/changes/0021/request.md`
- Slice map: `work/changes/0021/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/034-overlapping-ideas-need-pruning.md`
- `docs/episodes/035-pruned-pages-read-better.md`
- `docs/concepts/overlap-hurts-the-page-family-model.md`
- `docs/concepts/pruning-keeps-the-site-focused.md`
- `docs/notes/0018-content-pruning-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_seventeen.py`

## Impact Summary

This batch extends the knowledge layer with pages about removing overlap and
pruning redundant material.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- pruning is editorial maintenance, not deletion for its own sake
- overlapping ideas should not multiply across page families
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
