# Slice 0063 - Reference Pages Are Not Dumps

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

Add a concept page about reference pages staying selective and readable.

## In Scope

- create one concept page about reference pages not becoming dumps

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why reference pages need scope

## Main Business Rules

- reference pages should stay curated
- too many unrelated links reduce usefulness
- the page should stay focused on support material

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/reference-pages-are-not-dumps.md` exists
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
- the page reinforces selective reference use
- the change is represented in `work/changes/0016/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a directory of sources
