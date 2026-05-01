# Request Slice Map

- Change: `0027`
- Request: `work/changes/0027/request.md`
- Status: accepted

## Request Boundary

Add five pages that keep pack selection and MRL core separation explicit.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0115-packs-define-implementation-defaults.md` | accepted | Adds an episode page about packs defining implementation defaults. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentythree.py` |
| `docs/slices/0116-python-ddd-monolith-is-a-selected-pack.md` | accepted | Adds an episode page about the Python DDD monolith being a selected pack. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentythree.py` |
| `docs/slices/0117-mrl-core-is-separate-from-packs.md` | accepted | Adds a concept page about MRL core being separate from packs. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentythree.py` |
| `docs/slices/0118-runtime-topology-belongs-to-the-pack.md` | accepted | Adds a concept page about runtime topology belonging to the pack. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentythree.py` |
| `docs/slices/0119-pack-selection-workflow.md` | accepted | Adds a note page describing the pack selection workflow. | `tests/integration/test_knowledge_layer_next_five_pages_batch_twentythree.py` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice batch

## EGD Notes

Expectation-gap review should verify that pack choice is presented as an
implementation default, not as the definition of MRL itself.
