# Request Slice Map

- Change: `0002`
- Request: `work/changes/0002/request.md`
- Status: accepted

## Request Boundary

Create the first publishable Markdown knowledge-layer shell for the
`@umoutrohenrique` content system.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0002-github-pages-knowledge-layer-shell.md` | accepted | Covers the full request with the docs site shell, navigation, and publish guidance. | `tests/integration/test_knowledge_layer_site.py`, `docs/index.md`, `docs/episodes/index.md`, `docs/concepts/index.md`, `docs/references/index.md`, `docs/episodes/001-template.md`, `readme.md` |

## Out Of Scope

- custom domain and hosting infrastructure
- content automation
- CMS/editor integration
- database or search implementation

## Open Questions

- none for this slice

## EGD Notes

Expectation-gap review should verify that the site is markdown-first, that the
published docs root is easy to navigate, and that the README describes the
GitHub Pages publishing path clearly.

