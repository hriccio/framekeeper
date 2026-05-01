# Impact Analysis

- Change: `0027`
- Request: `work/changes/0027/request.md`
- Slice map: `work/changes/0027/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/046-packs-define-implementation-defaults.md`
- `docs/episodes/047-python-ddd-monolith-is-a-selected-pack.md`
- `docs/concepts/mrl-core-is-separate-from-packs.md`
- `docs/concepts/runtime-topology-belongs-to-the-pack.md`
- `docs/notes/0024-pack-selection-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_twentythree.py`

## Impact Summary

This batch extends the knowledge layer with pages about implementation packs
and their separation from MRL core.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- pack selection shapes implementation defaults
- MRL core stays separate from packs
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
