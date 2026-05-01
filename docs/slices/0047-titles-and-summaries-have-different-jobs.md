# Slice 0047 - Titles And Summaries Have Different Jobs

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

Add a concept page that says titles and summaries serve different jobs.

## In Scope

- create one concept page about titles and summaries
- link it to the episode pages that use those elements

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain the division of responsibility

## Main Business Rules

- titles and summaries are not interchangeable
- each should support the page in a different way
- the page should not become a metadata policy doc

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/titles-and-summaries-have-different-jobs.md` exists
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
- the page preserves the title-summary distinction
- the change is represented in `work/changes/0013/implementation.md`

## Resolved Design Decisions

- keep the page short and practical
- avoid collapsing it into page-shape guidance

