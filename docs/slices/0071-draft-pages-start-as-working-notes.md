# Slice 0071 - Draft Pages Start As Working Notes

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

Add an episode page that says draft pages start as working notes.

## In Scope

- create one episode page about draft pages starting as working notes
- link it to the concept and note pages that support the draft boundary

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain how a draft can become a public page

## Main Business Rules

- drafts are intermediate artifacts
- working notes can become public later
- the page should not become a checklist for publication

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/029-draft-pages-start-as-working-notes.md` exists
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
- the page reinforces draft-to-page progression
- the change is represented in `work/changes/0018/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a publishing process manual
