# Slice 0141 - Source-Rich Ideas Belong In References

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

Add an episode page about source-rich ideas belonging in references.

## In Scope

- create one episode page about using references for source-heavy ideas
- link it to the concept and note pages that support classification

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why source-heavy ideas fit references

## Main Business Rules

- source-heavy material should point to references
- the source should remain easy to find
- the page should not become a general essay

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/057-source-rich-ideas-belong-in-references.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the supporting concept and note pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces references as the right home for source-heavy ideas
- the change is represented in `work/changes/0032/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning references into a source dump
