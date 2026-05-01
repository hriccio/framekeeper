# Slice 0084 - Reference Refresh Workflow

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

Add a note page that records the reference refresh workflow.

## In Scope

- create one note page about refreshing references when they age

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe a repeatable refresh workflow

## Main Business Rules

- recheck the source before reuse
- update or replace references that have drifted
- keep the page focused on current evidence

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0017-reference-refresh-workflow.md` exists
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
- the page reinforces reference refresh work
- the change is represented in `work/changes/0020/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into an exhaustive source-audit manual
