# Slice 0043 - Reference Pages Need Scope

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

Add a concept page that explains why reference pages need scope.

## In Scope

- create one concept page about reference scope
- link it to the episode and note pages that motivate it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why references stay narrow and deliberate

## Main Business Rules

- references should support a clear purpose
- scoped references are easier to maintain
- the page should not become a source catalog guide

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/reference-pages-need-scope.md` exists
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
- the page preserves the scope boundary for references
- the change is represented in `work/changes/0012/implementation.md`

## Resolved Design Decisions

- keep the page scoped and practical
- avoid broad source-management guidance

