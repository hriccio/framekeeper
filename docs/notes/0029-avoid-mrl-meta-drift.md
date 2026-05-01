# Avoid MRL Meta Drift

## Purpose

This note records a guardrail for future sessions: keep knowledge-layer batches
focused on the channel and content domain, not on MRL process artifacts unless
the request explicitly asks for process work.

## Notes

- default batches should add domain-facing knowledge pages
- do not turn a content batch into a repository-process batch by accident
- only create request, slice, and implementation artifacts when the request is
  explicitly about workflow, traceability, or implementation structure
- if a proposed page mostly explains how the loop works, pause and confirm that
  the request really wants MRL-meta content
- when in doubt, ask whether the page should describe the channel subject
  matter or the repository process

## Related Pages

- [Request To Slice Workflow](./0028-request-to-slice-workflow.md)
- [Scenario Evaluation Workflow](./0025-scenario-evaluation-workflow.md)
- [Release And Exposure Workflow](./0026-release-and-exposure-workflow.md)
- [Feedback Capture Workflow](./0027-feedback-capture-workflow.md)
