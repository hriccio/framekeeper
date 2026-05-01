# Slice 0049 - Title Summary Workflow

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

Add a note page that records the workflow for keeping titles and summaries in
sync.

## In Scope

- create one note page about the title-summary workflow
- link it to the episode and concept pages that support the rule

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should explain how the title and summary stay aligned

## Main Business Rules

- titles and summaries should be revised together
- notes can describe the workflow, but they are not the page content
- the note should not turn into an editing checklist

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0010-title-summary-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow the links to the pages it references

## Done Criteria

- the note page exists and is linked
- the page preserves the title-summary workflow boundary
- the change is represented in `work/changes/0013/implementation.md`

## Resolved Design Decisions

- keep the note concise
- avoid turning it into a documentation style guide

