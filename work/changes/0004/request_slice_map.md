# Request Slice Map

- Change: `0004`
- Request: `work/changes/0004/request.md`
- Status: accepted

## Request Boundary

Extend the knowledge layer with the notes section and a single seeded note so
the site reflects the full content model from the handoff.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0004-knowledge-layer-notes-section.md` | accepted | Covers the full request by adding the notes section, a seeded note, and navigation links. | `tests/integration/test_knowledge_layer_notes_section.py`, `docs/index.md`, `docs/notes/index.md` |

## Out Of Scope

- automation and generation
- publishing infrastructure
- search and database support

## Open Questions

- none for this slice

## EGD Notes

Expectation-gap review should verify that notes are present as a distinct
knowledge-layer artifact type and that the new content does not blur into raw
transcript storage.

