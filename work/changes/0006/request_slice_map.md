# Request Slice Map

- Change: `0006`
- Request: `work/changes/0006/request.md`
- Status: accepted

## Request Boundary

Add five pages that describe the knowledge layer's publishing model and
repository boundaries.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0010-markdown-is-the-source-of-truth.md` | accepted | Adds an episode page that states markdown is the source of truth for the site. | `tests/integration/test_knowledge_layer_next_five_pages_batch_two.py` |
| `docs/slices/0011-github-pages-is-enough-for-now.md` | accepted | Adds an episode page that keeps the site grounded on GitHub Pages without extra infrastructure. | `tests/integration/test_knowledge_layer_next_five_pages_batch_two.py` |
| `docs/slices/0012-wnt-and-codingzen-stay-separate.md` | accepted | Adds a concept page that keeps the knowledge layer distinct from WastingNoTime and CodingZen. | `tests/integration/test_knowledge_layer_next_five_pages_batch_two.py` |
| `docs/slices/0013-manual-publishing-rhythm.md` | accepted | Adds a concept page that favors continuity and manual editing over optimization. | `tests/integration/test_knowledge_layer_next_five_pages_batch_two.py` |
| `docs/slices/0014-published-content-is-not-raw-evidence.md` | accepted | Adds a note page that describes the boundary between published content and raw evidence. | `tests/integration/test_knowledge_layer_next_five_pages_batch_two.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the pages encode the repository's
editorial policy clearly and do not blur the knowledge layer with raw input or
other site families.

