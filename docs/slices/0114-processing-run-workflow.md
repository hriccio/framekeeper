# Slice 0114 - Processing Run Workflow

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

Add a note page that records the processing run workflow.

## In Scope

- create one note page about the processing run trace

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how the run remains inspectable

## Main Business Rules

- record the run as a traceable step
- keep transcript and metadata together
- preserve enough context for later review

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0023-processing-run-workflow.md` exists
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
- the page reinforces the processing-run workflow
- the change is represented in `work/changes/0026/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a runbook
