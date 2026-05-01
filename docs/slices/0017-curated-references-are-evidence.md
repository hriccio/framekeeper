# Slice 0017 - Curated References Are Evidence

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

Add a concept page that frames curated references as supporting evidence rather
than decorative links.

## In Scope

- create one concept page about curated references
- link it back to the episode pages that use it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should define why references matter

## Main Business Rules

- references should support claims and context
- curation should be deliberate
- the concept page should avoid becoming a generic citation policy

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/curated-references-are-evidence.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the episode and reference pages

## Done Criteria

- the concept page exists and is linked
- the page preserves the evidence role of references
- the change is represented in `work/changes/0007/implementation.md`

## Resolved Design Decisions

- write the page as a reusable concept
- keep the language strict enough to guide future curation

