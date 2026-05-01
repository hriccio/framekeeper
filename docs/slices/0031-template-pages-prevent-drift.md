# Slice 0031 - Template Pages Prevent Drift

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

Add an episode page that explains how templates prevent drift across pages.

## In Scope

- create one episode page about templates
- link it to the template page and related concept pages

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should describe why templates matter

## Main Business Rules

- templates should reduce variation where consistency matters
- templates should not erase useful editorial judgment
- the page should not become a doc-tooling manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/013-template-pages-prevent-drift.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the template and supporting concept pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces template use as a maintenance aid
- the change is represented in `work/changes/0010/implementation.md`

## Resolved Design Decisions

- keep the page focused on drift reduction
- avoid broadening it into repository design advice

