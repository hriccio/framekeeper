# Slice 0144 - Transcript Classification Checklist

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

Add a note page that records the transcript classification checklist.

## In Scope

- create one note page about classifying transcript-derived ideas
- link it to the episode and concept pages that support the checklist

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should describe how to choose the right page family

## Main Business Rules

- identify the main angle first
- decide whether the source is the point
- choose the page family that matches the idea's main job

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0030-transcript-classification-checklist.md` exists
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
- the page records the transcript classification checklist
- the change is represented in `work/changes/0032/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid collapsing the checklist into a general writing guide
