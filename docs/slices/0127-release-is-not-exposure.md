# Slice 0127 - Release Is Not Exposure

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

Add a concept page about release not being the same as exposure.

## In Scope

- create one concept page about the distinction between release and exposure
- connect it to the release and exposure episodes

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain the boundary between acceptance and exposure

## Main Business Rules

- release is internal acceptance
- exposure is the operational follow-through
- the two steps should stay separate in the workflow

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/052-release-is-not-exposure.md` exists
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
- the page keeps release and exposure separate
- the change is represented in `work/changes/0029/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making exposure look like release by another name
