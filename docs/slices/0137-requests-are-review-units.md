# Slice 0137 - Requests Are Review Units

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

Add a concept page about requests being review units.

## In Scope

- create one concept page about the request as the review boundary
- connect it to the request boundary episode pages

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why the request stays the review unit

## Main Business Rules

- the request is the boundary for expectation review
- slices support the request but do not replace it
- implementation must not redefine the goal

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/056-requests-are-review-units.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode and note pages

## Done Criteria

- the concept page exists and is linked
- the page keeps the request as the review unit
- the change is represented in `work/changes/0031/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid blending request and build artifacts
