# Slice 0010 - Markdown Is The Source Of Truth

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

Add an episode page that says markdown is the source of truth for the knowledge
layer.

## In Scope

- create one episode page about markdown-first publishing
- link it back to the home page and to related concept pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should favor markdown over generated HTML or CMS content

## Main Business Rules

- markdown is the source of truth
- published pages should remain easy to edit in Git
- the episode page should not become a tooling manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/004-markdown-is-the-source-of-truth.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the related concept and note pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces the markdown-first rule
- the change is represented in `work/changes/0006/implementation.md`

## Resolved Design Decisions

- keep the page short and normative
- avoid introducing site-generator language into the page

