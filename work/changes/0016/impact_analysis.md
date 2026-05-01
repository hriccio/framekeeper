# Impact Analysis

- Change: `0016`
- Request: `work/changes/0016/request.md`
- Slice map: `work/changes/0016/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/024-references-should-stay-targeted.md`
- `docs/episodes/025-source-links-need-an-anchor.md`
- `docs/concepts/claims-and-sources-stay-paired.md`
- `docs/concepts/reference-pages-are-not-dumps.md`
- `docs/notes/0013-reference-review-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_twelve.py`

## Impact Summary

This batch extends the knowledge layer with pages about reference discipline
and source grounding.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- references remain curated support material, not exhaustive archives
- source links stay anchored to the claims they support
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
