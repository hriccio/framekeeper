# Slice 0062 - Claims And Sources Stay Paired

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

Add a concept page about keeping claims and sources close together.

## In Scope

- create one concept page about claims and sources staying paired

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why sources belong near claims

## Main Business Rules

- claims should not float away from their evidence
- the source should stay readable next to the claim
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/claims-and-sources-stay-paired.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode pages

## Done Criteria

- the concept page exists and is linked
- the page reinforces claim-source pairing
- the change is represented in `work/changes/0016/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making it a policy page
