# Safety Vs Signal

Safety and signal are separate concerns.

## Meaning

Safety is the hard constraint that can stop the workflow. Signal is soft
diagnostic feedback that should help interpretation without controlling output.

## Related Episodes

- [Automation Handles Mechanics](../episodes/002-automation-handles-mechanics.md)
- [Safety Is The Hard Gate](../episodes/003-safety-is-the-hard-gate.md)

## Notes

- keep the two layers structurally separate
- avoid quality language that reads like a hidden gate
- preserve the diagnostic nature of signal feedback

