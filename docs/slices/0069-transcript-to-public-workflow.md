# Slice 0069 - Transcript To Public Workflow

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

Add a note page that records the transcript-to-public workflow.

## In Scope

- create one note page about the boundary from transcript material to public
  content

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe a repeatable transcript-to-public process

## Main Business Rules

- transcripts stay in the working layer
- ideas are extracted before publication
- public pages are intentionally selected

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0014-transcript-to-public-workflow.md` exists
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
- the page reinforces the transcript-to-public boundary
- the change is represented in `work/changes/0017/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a detailed operational manual
