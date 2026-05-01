# Slice 0044 - Page Family Map

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

Add a note page that records the page family map for the site.

## In Scope

- create one note page about the page family map
- link it to the episode and concept pages that support the model

## Use-Case Contract

- input: manually authored note content
- output: one structured note page under `docs/notes/`
- behavior: the note should explain how the page families fit together

## Main Business Rules

- page families should stay distinct
- the family map should be easy to scan
- the note should not turn into a full site architecture manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/notes/0009-page-family-map.md` exists
- the home page links to the page
- the notes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the notes index lists the page

## Scenario Definition

1. open the note page
2. follow the links to the pages it references

## Done Criteria

- the note page exists and is linked
- the page preserves the family-map boundary
- the change is represented in `work/changes/0012/implementation.md`

## Resolved Design Decisions

- keep the note concise
- avoid turning it into repository structure guidance

