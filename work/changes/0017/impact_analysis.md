# Impact Analysis

- Change: `0017`
- Request: `work/changes/0017/request.md`
- Slice map: `work/changes/0017/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/026-raw-transcripts-stay-private.md`
- `docs/episodes/027-public-pages-are-refined.md`
- `docs/concepts/raw-evidence-is-not-the-site.md`
- `docs/concepts/public-content-needs-selection.md`
- `docs/notes/0014-transcript-to-public-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_thirteen.py`

## Impact Summary

This batch extends the knowledge layer with pages about the boundary between
raw transcript material and public site content.

The home page and section indices need to surface the new pages so readers can
reach them from the existing navigation structure.

The content stays manual and markdown-first. No automation, publishing
infrastructure, or transcript-processing behavior is introduced.

## Boundary Notes

- raw transcripts stay private working material
- public pages should stay refined and selective
- the batch remains within the public knowledge layer

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
