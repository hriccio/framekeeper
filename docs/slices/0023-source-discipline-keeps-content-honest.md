# Slice 0023 - Source Discipline Keeps Content Honest

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

Add a concept page that keeps source discipline strict and visible.

## In Scope

- create one concept page about source discipline
- link it to the source-aware episode and note pages

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why sources matter for honesty

## Main Business Rules

- source discipline is part of editorial integrity
- source paths should remain explicit
- the page should not become a generic policy note

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/source-discipline-keeps-content-honest.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow the links to the source-aware episode and note pages

## Done Criteria

- the concept page exists and is linked
- the page preserves the source discipline rule
- the change is represented in `work/changes/0008/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid expanding it into a general source policy manual

