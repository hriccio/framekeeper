# Slice 0128 - Portable Artifacts Support Exposure

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

Add a concept page about portable artifacts supporting exposure.

## In Scope

- create one concept page about the form of the released artifact
- connect it to the release and exposure episodes

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why exposed artifacts need a portable form

## Main Business Rules

- exposed artifacts should travel cleanly into the real context
- the artifact should be identifiable as the accepted release
- the internal loop should not be embedded in the exposed form

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/053-portable-artifacts-support-exposure.md` exists
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
- the page explains why exposed artifacts should be portable
- the change is represented in `work/changes/0029/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning exposure packaging into operations doctrine
