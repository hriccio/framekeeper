# Slice 0136 - Slice Maps Make Coverage Visible

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

Add an episode page about slice maps making coverage visible.

## In Scope

- create one episode page about traceability between request and slices
- link it to the concept and note pages that support build work

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why slice maps make coverage visible

## Main Business Rules

- slice maps should be explicit
- slice maps are traceability artifacts
- slice maps should not be treated as implementation code

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/055-slice-maps-make-coverage-visible.md` exists
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
- the page reinforces slice-map traceability
- the change is represented in `work/changes/0031/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning traceability into code generation
