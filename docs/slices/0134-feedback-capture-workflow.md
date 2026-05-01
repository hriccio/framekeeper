# Slice 0134 - Feedback Capture Workflow

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

Add a note page that records the feedback capture workflow.

## In Scope

- create one note page about capturing post-exposure feedback
- link it to the episode and concept pages that support the workflow

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how feedback becomes the next loop input

## Main Business Rules

- observe the real context
- record surprises, friction, and drift
- turn the observations into the next request or refinement

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0027-feedback-capture-workflow.md` exists
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
- the page records the feedback capture workflow
- the change is represented in `work/changes/0030/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid collapsing feedback capture into signal scoring
