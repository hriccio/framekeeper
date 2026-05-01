# Slice 0042 - Page Families Have Different Jobs

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

Add a concept page that states page families have different jobs.

## In Scope

- create one concept page about page-family roles
- link it to the episode pages that use the distinction

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should define the family roles clearly

## Main Business Rules

- episodes, concepts, references, and notes are not interchangeable
- each family serves a different editorial purpose
- the page should not become a full content-model specification

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/page-families-have-different-jobs.md` exists
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
- the page preserves the family-role distinction
- the change is represented in `work/changes/0012/implementation.md`

## Resolved Design Decisions

- keep the page short and explanatory
- avoid duplicating the individual page-type notes

