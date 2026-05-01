# Slice 0024 - Adding New Pages Workflow

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

Add a note page that describes the workflow for adding new knowledge-layer
pages.

## In Scope

- create one note page about adding pages
- link it to the pages that motivate the workflow

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should describe how to extend the site cleanly

## Main Business Rules

- new pages should stay linked from the home page and indices
- note pages can explain workflow, but they are not content buckets
- the note should not turn into a repository operations manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0005-adding-new-pages-workflow.md` exists
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
- the page preserves the extension workflow
- the change is represented in `work/changes/0008/implementation.md`

## Resolved Design Decisions

- keep the note short and procedural
- avoid duplicating the root docs guidance

