# Slice 0064 - Reference Review Workflow

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

Add a note page that records the workflow for reviewing references.

## In Scope

- create one note page about reviewing references before linking them

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe a repeatable reference review workflow

## Main Business Rules

- confirm the source supports the claim
- keep the linked set as small as possible
- preserve readability after the links are added

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0013-reference-review-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow links to the related concept and episode pages

## Done Criteria

- the note page exists and is linked
- the page reinforces repeatable reference review
- the change is represented in `work/changes/0016/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making it an exhaustive citation process
