# Slice 0027 - Drafts Are Not Final

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

Add a concept page that states drafts are not final content.

## In Scope

- create one concept page about draft status
- link it to the episode pages that use it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should define the status boundary clearly

## Main Business Rules

- drafts are intermediate work
- refined pages are the published content layer
- the page should not blur draft and final states

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/drafts-are-not-final.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the episode and note pages it references

## Done Criteria

- the concept page exists and is linked
- the page preserves the draft status boundary
- the change is represented in `work/changes/0009/implementation.md`

## Resolved Design Decisions

- keep the page as a boundary statement
- avoid turning it into a note about task management

