# Impact Analysis

- Change: `0026`
- Request: `work/changes/0026/request.md`
- Slice map: `work/changes/0026/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/044-processing-runs-stay-inspectable.md`
- `docs/episodes/045-transcripts-and-metadata-travel-together.md`
- `docs/concepts/inspectable-runs-need-clear-artifacts.md`
- `docs/concepts/transcripts-are-intermediate-artifacts.md`
- `docs/notes/0023-processing-run-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_twentytwo.py`

## Impact Summary

This batch extends the knowledge layer with pages about repeatable processing
runs and the artifacts they produce.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- processing runs should be inspectable
- transcripts and metadata belong together as intermediate artifacts
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
