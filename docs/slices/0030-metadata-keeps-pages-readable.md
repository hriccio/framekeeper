# Slice 0030 - Metadata Keeps Pages Readable

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

Add an episode page that says metadata keeps pages readable and reusable.

## In Scope

- create one episode page about metadata
- link it back to the concept and note pages that motivate it

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should show why metadata belongs on the page

## Main Business Rules

- metadata should make pages easier to scan
- metadata should support reuse and traceability
- the page should not become a style guide

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/012-metadata-keeps-pages-readable.md` exists
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
- the page reinforces the metadata discipline
- the change is represented in `work/changes/0010/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a page schema spec

