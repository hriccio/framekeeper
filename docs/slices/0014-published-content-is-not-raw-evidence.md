# Slice 0014 - Published Content Is Not Raw Evidence

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

Add a note page that states the boundary between published knowledge-layer
content and raw evidence.

## In Scope

- create one note page about published content versus raw evidence
- link it to the related episode and concept pages

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the page should explain why raw evidence stays outside the site

## Main Business Rules

- raw evidence is preserved under `work/sources/`
- published content belongs under `docs/`
- the note page should not contain raw transcript blobs

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0003-published-content-is-not-raw-evidence.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow links to the pages it references

## Done Criteria

- the note page exists and is linked
- the page preserves the raw-evidence boundary
- the change is represented in `work/changes/0006/implementation.md`

## Resolved Design Decisions

- keep the note concise and boundary-focused
- avoid letting the note become a storage policy document

