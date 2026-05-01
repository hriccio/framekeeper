# Scenario Evaluation Is Not Tests

## Metadata

- YouTube channel: `@umoutrohenrique`
- Status: refined

---

## Core idea

Scenario evaluation complements tests, but it does not replace them.

## What I said

The repository needs a review loop that can ask whether the behavior feels
complete, not just whether it passes assertions. That is different from normal
correctness testing.

## Key points

- tests check invariants and contracts
- scenario evaluation checks semantic completeness
- expectation gaps are review questions, not automatic failures

## Related Concepts

- [Validation Modes Guide Slice Strategy](../concepts/validation-modes-guide-slice-strategy.md)
- [Deterministic Packets Keep Evidence Reviewable](../concepts/deterministic-packets-keep-evidence-reviewable.md)

## References

- [Scenario Evaluation](../evaluation/scenario_evaluation.md)

## Refined conclusion

The evaluation loop should expose omissions without pretending to be the test
suite.
