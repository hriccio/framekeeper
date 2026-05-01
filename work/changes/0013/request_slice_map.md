# Request Slice Map

- Change: `0013`
- Request: `work/changes/0013/request.md`
- Status: accepted

## Request Boundary

Add five pages that clarify the role of titles and summaries in the knowledge
layer.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0045-titles-should-match-the-idea.md` | accepted | Adds an episode page about titles matching the idea. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nine.py` |
| `docs/slices/0046-summaries-preserve-gist.md` | accepted | Adds an episode page about summaries preserving gist. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nine.py` |
| `docs/slices/0047-titles-and-summaries-have-different-jobs.md` | accepted | Adds a concept page about titles and summaries having different jobs. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nine.py` |
| `docs/slices/0048-gist-should-stay-aligned.md` | accepted | Adds a concept page about gist staying aligned with the page. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nine.py` |
| `docs/slices/0049-title-summary-workflow.md` | accepted | Adds a note page describing the title-summary workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_nine.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that titles and summaries remain supportive
of the content, not a substitute for it.

