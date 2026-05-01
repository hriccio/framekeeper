# Slice 0072 - Extraction Turns Transcripts Into Candidates

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

Add a concept page about extraction creating candidate ideas from transcripts.

## In Scope

- create one concept page about extraction turning transcripts into candidates

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why extraction is selective

## Main Business Rules

- transcripts become candidates, not final pages
- extraction should preserve reusable ideas
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/extraction-turns-transcripts-into-candidates.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode pages

## Done Criteria

- the concept page exists and is linked
- the page reinforces extraction as a filtering step
- the change is represented in `work/changes/0018/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making it a workflow checklist
