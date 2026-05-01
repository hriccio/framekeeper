# Impact Analysis

- Change: `0019`
- Request: `work/changes/0019/request.md`
- Slice map: `work/changes/0019/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/030-candidate-ideas-need-a-family.md`
- `docs/episodes/031-references-become-reference-pages.md`
- `docs/concepts/family-assignment-keeps-drafts-clear.md`
- `docs/concepts/draft-candidates-need-a-destination.md`
- `docs/notes/0016-candidate-promotion-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_fifteen.py`

## Impact Summary

This batch extends the knowledge layer with pages about assigning extracted
candidates to the correct page family.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- candidate ideas should not stay family-less for long
- references and concepts have different destinations
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
