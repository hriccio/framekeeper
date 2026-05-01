# Slice 0053 - Home Pages Should Favor Signal

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

Add a concept page that says home pages should favor signal over breadth.

## In Scope

- create one concept page about home-page curation
- link it to the episode and note pages that support the idea

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why the home page stays selective

## Main Business Rules

- home pages should show the strongest signals first
- breadth should not overwhelm the front door
- the page should not become a generic homepage best-practices doc

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/home-pages-should-favor-signal.md` exists
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
- the page preserves the selective front-door boundary
- the change is represented in `work/changes/0014/implementation.md`

## Resolved Design Decisions

- keep the page focused on selection, not ranking
- avoid turning it into a UX guideline document

