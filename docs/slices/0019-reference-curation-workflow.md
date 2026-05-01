# Slice 0019 - Reference Curation Workflow

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

Add a note page that records the workflow for curating references into the
knowledge layer.

## In Scope

- create one note page about reference curation
- link it to the relevant episode, concept, and reference pages

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should explain how references are selected and used

## Main Business Rules

- references are curated, not auto-generated
- note pages may explain workflow, but they are not source libraries
- the note page should preserve the distinction between evidence and output

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0004-reference-curation-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow links to the pages it references

## Done Criteria

- the note page exists and is linked
- the page preserves the curation workflow boundary
- the change is represented in `work/changes/0007/implementation.md`

## Resolved Design Decisions

- keep the note short and operational
- avoid letting it become a general documentation policy

