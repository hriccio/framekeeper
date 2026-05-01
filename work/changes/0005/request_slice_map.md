# Request Slice Map

- Change: `0005`
- Request: `work/changes/0005/request.md`
- Status: accepted

## Request Boundary

Add five content pages that deepen the knowledge layer around the channel's
core operating principles and content routing.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0005-automation-handles-mechanics.md` | accepted | Adds an episode page about automation staying on the mechanical side of the workflow. | `tests/integration/test_knowledge_layer_content_seed.py` |
| `docs/slices/0006-safety-is-the-hard-gate.md` | accepted | Adds an episode page about safety being the only blocking stage. | `tests/integration/test_knowledge_layer_next_five_pages.py` |
| `docs/slices/0007-human-final-authority.md` | accepted | Adds a concept page that states Henrique remains the final authority over meaning and publication. | `tests/integration/test_knowledge_layer_next_five_pages.py` |
| `docs/slices/0008-safety-vs-signal.md` | accepted | Adds a concept page that keeps the hard safety gate separate from soft diagnostic signal. | `tests/integration/test_knowledge_layer_next_five_pages.py` |
| `docs/slices/0009-raw-and-refined-routing.md` | accepted | Adds a note page describing how raw evidence becomes refined knowledge-layer content. | `tests/integration/test_knowledge_layer_next_five_pages.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that the pages reinforce the repository's
existing principles without collapsing raw and refined material together.

