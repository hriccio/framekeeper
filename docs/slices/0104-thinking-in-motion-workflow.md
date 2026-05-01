# Slice 0104 - Thinking In Motion Workflow

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

Add a note page that records the thinking-in-motion workflow.

## In Scope

- create one note page about moving from live recording to durable page

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how the idea is preserved after recording

## Main Business Rules

- treat the recording as source material
- extract the reusable idea
- shape the idea into a page that stands alone

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0021-thinking-in-motion-workflow.md` exists
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
- the page reinforces the thinking-in-motion workflow
- the change is represented in `work/changes/0024/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a transcript handling manual
