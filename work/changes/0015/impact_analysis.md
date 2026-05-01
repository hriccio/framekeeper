# Impact Analysis

- Change: `0015`
- Request: `work/changes/0015/request.md`
- Slice map: `work/changes/0015/request_slice_map.md`

## Areas Affected

- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/episodes/022-broken-links-are-regressions.md`
- `docs/episodes/023-reading-paths-should-stay-obvious.md`
- `docs/concepts/link-hygiene-keeps-the-site-trustworthy.md`
- `docs/concepts/reading-path-is-part-of-editing.md`
- `docs/notes/0012-link-checking-workflow.md`
- `tests/integration/test_knowledge_layer_next_five_pages_batch_eleven.py`

## Impact Summary

This batch extends the knowledge layer with pages about link hygiene and the
reader's path through the site.

The home page and section indices now need to surface the new pages so readers
can reach them from the existing navigation structure.

The new pages stay within the manually authored, markdown-first pattern already
used by the knowledge layer. No automation, publishing infrastructure, or
transcript-processing behavior is introduced by this batch.

## Boundary Notes

- broken links are treated as editorial regressions, not as content trivia
- reading paths remain part of page editing, not a separate navigation system
- the batch stays within the public knowledge layer and does not touch the
  transcript pipeline

## Verification Notes

- the integration test should confirm the new files exist
- the integration test should confirm the home page and indices link the new
  pages
