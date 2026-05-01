# Slice 0052 - Curated Entry Points Reduce Friction

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

Add a concept page that says curated entry points reduce friction.

## In Scope

- create one concept page about curated entry points
- link it to the episode pages that motivate curation

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why curated links help readers move faster

## Main Business Rules

- curated entry points should be easy to scan
- the home page should reduce friction rather than raise it
- the page should not become a design manifesto

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/curated-entry-points-reduce-friction.md` exists
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
- the page preserves the friction-reduction boundary
- the change is represented in `work/changes/0014/implementation.md`

## Resolved Design Decisions

- keep the page practical
- avoid broadening it into site UX theory

