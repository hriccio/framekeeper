# Impact Analysis

- Change: `0025`
- Request: `work/changes/0025/request.md`
- Slice map: `work/changes/0025/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/042-work-sources-hold-raw-evidence.md`
- `docs/episodes/043-work-changes-preserve-loop-history.md`
- `docs/concepts/memory-is-split-by-purpose.md`
- `docs/concepts/change-artifacts-keep-the-loop-readable.md`
- `docs/notes/0022-repository-memory-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_twentyone.py`

## Impact Summary

This batch extends the knowledge layer with pages about repository memory and
loop history.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- raw evidence belongs in `work/sources`
- change artifacts preserve the history of the loop
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
