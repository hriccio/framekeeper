# Slice 0124 - Scenario Evaluation Workflow

## Status

Accepted.

## Selected Pack

- documentation-first, no runtime pack change

## Runtime Targets

- GitHub Pages from `docs/`
- local markdown browsing and link checking

## Architecture Mode

- static markdown content layer
- manual authorship first

## Intent

Add a note page that records the practical scenario evaluation workflow.

## In Scope

- create one note page about scenario evaluation
- link it to the episode and concept pages that support the workflow

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe the evaluation loop in practical terms

## Main Business Rules

- run a deterministic scenario before review
- capture machine-readable evidence
- decide whether the request needs refinement

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0025-scenario-evaluation-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow links to the related episode and concept pages

## Done Criteria

- the note page exists and is linked
- the page records the scenario evaluation workflow
- the change is represented in `work/changes/0028/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a full evaluation manual
