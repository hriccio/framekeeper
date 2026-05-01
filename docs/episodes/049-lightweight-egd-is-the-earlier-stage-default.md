# Lightweight EGD Is The Earlier-Stage Default

## Metadata

- YouTube channel: `@umoutrohenrique`
- Status: refined

---

## Core idea

When deterministic scenario evidence is not available yet, lightweight EGD is
the normal review mode.

## What I said

If there is no scenario packet, the review should use the semantic artifacts,
implementation artifacts, and recent test evidence that already exist. It
should not pretend that a fuller scenario run happened.

## Key points

- lightweight EGD is an expected earlier-stage mode
- artifact-led review is enough before scenario infrastructure exists
- the review boundary stays the request, not the raw test output

## Related Concepts

- [Validation Modes Guide Slice Strategy](../concepts/validation-modes-guide-slice-strategy.md)
- [Deterministic Packets Keep Evidence Reviewable](../concepts/deterministic-packets-keep-evidence-reviewable.md)

## References

- [Scenario Evaluation](../evaluation/scenario_evaluation.md)

## Refined conclusion

Lightweight EGD is how the loop stays honest before deterministic scenario
packets exist.
