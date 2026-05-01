# Request Slice Map

- Change: `0016`
- Request: `work/changes/0016/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep reference curation and claim grounding explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0060-references-should-stay-targeted.md` | accepted | Adds an episode page about keeping references targeted. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twelve.py` |
| `docs/slices/0061-source-links-need-an-anchor.md` | accepted | Adds an episode page about source links needing an anchor in the claim. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twelve.py` |
| `docs/slices/0062-claims-and-sources-stay-paired.md` | accepted | Adds a concept page about pairing claims with sources. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twelve.py` |
| `docs/slices/0063-reference-pages-are-not-dumps.md` | accepted | Adds a concept page about reference pages staying selective. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twelve.py` |
| `docs/slices/0064-reference-review-workflow.md` | accepted | Adds a note page describing the reference review workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twelve.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that references stay supportive rather
than becoming a dumping ground for unrelated links.
