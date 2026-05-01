# Slice 0029 - Draft To Refined Workflow

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

Add a note page that records the workflow for moving content from draft to
refined form.

## In Scope

- create one note page about the draft-to-refined workflow
- link it to the episode and concept pages that motivate it

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should explain how the publishing cycle is kept explicit

## Main Business Rules

- drafts are intermediate artifacts
- refined pages are the published ones
- the note should not turn into a task tracker

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0006-draft-to-refined-workflow.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow the links to the supporting pages

## Done Criteria

- the note page exists and is linked
- the page preserves the draft-to-refined workflow
- the change is represented in `work/changes/0009/implementation.md`

## Resolved Design Decisions

- keep the note short and actionable
- avoid duplicating the root docs guidance

