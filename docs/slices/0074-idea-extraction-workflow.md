# Slice 0074 - Idea Extraction Workflow

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

Add a note page that records the idea extraction workflow.

## In Scope

- create one note page about moving from transcript to draft candidate

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe a repeatable extraction workflow

## Main Business Rules

- read the transcript for candidate ideas
- separate reusable ideas from one-off phrasing
- capture the idea in a draft page or note

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0015-idea-extraction-workflow.md` exists
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
- the page reinforces idea extraction as a workflow
- the change is represented in `work/changes/0018/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a transcription playbook
