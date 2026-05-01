# Impact Analysis

- Change: `0020`
- Request: `work/changes/0020/request.md`
- Slice map: `work/changes/0020/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/032-sources-need-refresh-cycles.md`
- `docs/episodes/033-policy-references-age-over-time.md`
- `docs/concepts/source-currency-keeps-trust-intact.md`
- `docs/concepts/reference-drift-needs-review.md`
- `docs/notes/0017-reference-refresh-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_sixteen.py`

## Impact Summary

This batch extends the knowledge layer with pages about refreshing sources and
keeping policy references current.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- source currency is part of trust maintenance
- references age and need review
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
