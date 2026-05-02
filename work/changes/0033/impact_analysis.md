# Impact Analysis

## Scope

This change adds one application use case, one domain classifier, and one unit
test module.

## Affected Areas

- `src/app/domain/`
- `src/app/application/`
- `tests/unit/`
- `docs/slices/0145-transcript-idea-family-classification.md`

## Tension To Watch

The classifier should stay on the content side of the boundary. It is a
recommendation tool for page-family selection, not a safety gate and not a
publishing rule.

## Regression Risk

Low. The change is deterministic and isolated, but the cue precedence should be
kept stable because the tests depend on it.
