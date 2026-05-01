# Slice 0028 - Review Preserves Context

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

Add a concept page that says review should preserve context and intent.

## In Scope

- create one concept page about review
- link it to the episode and note pages that motivate it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should describe review as context-preserving, not context-stripping

## Main Business Rules

- review should keep origin and intent visible
- review should improve clarity without erasing meaning
- the page should not become a quality rubric

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/review-preserves-context.md` exists
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
- the page preserves the review/context boundary
- the change is represented in `work/changes/0009/implementation.md`

## Resolved Design Decisions

- keep the page focused on review semantics
- avoid introducing a hidden quality gate

