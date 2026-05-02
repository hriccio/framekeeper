# Slice 0145 - Transcript Idea Family Classification

## Status

Accepted.

## Selected Pack

- `python_ddd_monolith`

## Runtime Targets

- single Python runtime
- local deterministic execution for tests and scenario checks

## Architecture Mode

- DDD-inspired modular monolith
- thin application use case over deterministic domain components

## Intent

Classify transcript-derived ideas into the public knowledge-layer family they
best fit: episode, concept, reference, or note.

## In Scope

- implement a deterministic family classifier for transcript-derived ideas
- keep the classifier independent from safety scoring
- return a clear family recommendation with a readable rationale

## Use-Case Contract

- input: registered video submission with title and transcript
- output: a family recommendation for episode, concept, reference, or note
- behavior: source-heavy ideas should point to references, workflow ideas to
  notes, explanatory ideas to concepts, and everything else should default to
  episodes

## Main Business Rules

- page family follows editorial angle and evidence weight
- classification must not affect safety risk
- the recommendation must stay deterministic

## Required Ports

- none

## Out Of Scope

- automatic publishing
- workflow tracing artifacts
- knowledge-layer content generation

## Candidate Acceptance Criteria

- a transcript submission can be classified into one family recommendation
- source-heavy material maps to `REFERENCE`
- workflow/checklist material maps to `NOTE`
- explanatory material maps to `CONCEPT`
- generic narrative material defaults to `EPISODE`

## Initial Test Plan

- unit tests cover the family classifier for the four family shapes

## Scenario Definition

1. classify a source-heavy transcript fragment
2. classify a workflow-oriented transcript fragment
3. classify an explanatory transcript fragment
4. classify a generic narrative transcript fragment

## Done Criteria

- the classifier is implemented in code
- tests prove the family recommendations are deterministic
- the implementation does not change the safety/signal workflow
