# Request Slice Map

- Change: `0015`
- Request: `work/changes/0015/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep link hygiene and reading paths explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0055-broken-links-are-regressions.md` | accepted | Adds an episode page about broken links as regressions. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eleven.py` |
| `docs/slices/0056-reading-paths-should-stay-obvious.md` | accepted | Adds an episode page about keeping reading paths obvious. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eleven.py` |
| `docs/slices/0057-link-hygiene-keeps-the-site-trustworthy.md` | accepted | Adds a concept page about link hygiene and trust. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eleven.py` |
| `docs/slices/0058-reading-path-is-part-of-editing.md` | accepted | Adds a concept page about the reading path as an editorial concern. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eleven.py` |
| `docs/slices/0059-link-checking-workflow.md` | accepted | Adds a note page describing the link checking workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_eleven.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that broken links, reading paths, and link
checking are treated as maintenance concerns rather than content inflation.

