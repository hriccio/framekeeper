# Impact Analysis

- Change: `0024`
- Request: `work/changes/0024/request.md`
- Slice map: `work/changes/0024/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/040-videos-capture-thinking-in-motion.md`
- `docs/episodes/041-refined-pages-preserve-the-idea.md`
- `docs/concepts/exploratory-videos-need-extraction.md`
- `docs/concepts/durable-pages-outlast-the-recording.md`
- `docs/notes/0021-thinking-in-motion-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_twenty.md`

## Impact Summary

This batch extends the knowledge layer with pages about the relation between
exploratory videos and durable pages.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- recordings capture motion, not final doctrine
- extracted pages preserve the idea
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
