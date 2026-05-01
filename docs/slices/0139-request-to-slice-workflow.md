# Slice 0139 - Request To Slice Workflow

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

Add a note page that describes the request-to-slice workflow.

## In Scope

- create one note page about mapping request to slice work
- link it to the episode and concept pages that support the workflow

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how request boundaries become slices

## Main Business Rules

- define the request boundary first
- map the request to bounded slices
- keep slice docs separate from implementation code

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0028-request-to-slice-workflow.md` exists
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
- the page records the request-to-slice workflow
- the change is represented in `work/changes/0031/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid collapsing traceability into code generation
