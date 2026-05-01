# Request Slice Map

- Change: `0014`
- Request: `work/changes/0014/request.md`
- Status: accepted

## Request Boundary

Add five pages that document the curation of the site's front door.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0050-home-page-is-a-curated-entry-point.md` | accepted | Adds an episode page about the home page as a curated entry point. | `tests/integration/test_knowledge_layer_next_five_pages_batch_ten.py` |
| `docs/slices/0051-featured-links-should-stay-selective.md` | accepted | Adds an episode page about keeping featured links selective. | `tests/integration/test_knowledge_layer_next_five_pages_batch_ten.py` |
| `docs/slices/0052-curated-entry-points-reduce-friction.md` | accepted | Adds a concept page about curated entry points reducing friction. | `tests/integration/test_knowledge_layer_next_five_pages_batch_ten.py` |
| `docs/slices/0053-home-pages-should-favor-signal.md` | accepted | Adds a concept page about home pages favoring signal over breadth. | `tests/integration/test_knowledge_layer_next_five_pages_batch_ten.py` |
| `docs/slices/0054-front-door-curation-workflow.md` | accepted | Adds a note page describing the front-door curation workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_ten.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the front door stays selective,
readable, and clearly linked without trying to surface every page equally.

