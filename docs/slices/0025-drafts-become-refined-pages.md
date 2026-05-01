# Slice 0025 - Drafts Become Refined Pages

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

Add an episode page that explains how drafts become refined pages.

## In Scope

- create one episode page about moving from draft to refined form
- link it to the note and concept pages that support the workflow

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain the change from draft to refined content

## Main Business Rules

- drafts are intermediate, not final
- refined pages should be the published knowledge layer
- the page should not turn into a process checklist

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/010-drafts-become-refined-pages.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the supporting concept and note pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces the draft-to-refined transition
- the change is represented in `work/changes/0009/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a workflow spec

