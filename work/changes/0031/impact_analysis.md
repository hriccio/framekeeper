# Impact Analysis

## Scope

This batch only adds knowledge-layer documentation and the tests that prove the
new pages are linked.

## Affected Areas

- `docs/episodes/`
- `docs/concepts/`
- `docs/notes/`
- `docs/index.md`
- `docs/episodes/index.md`
- `docs/concepts/index.md`
- `docs/notes/index.md`
- `docs/slices/`
- `tests/integration/`

## Tension To Watch

The pages must keep request boundaries distinct from implementation details.
The wording should not imply that slice maps define the code itself.

## Regression Risk

Low. The change is additive and should only affect documentation navigation and
test coverage.
