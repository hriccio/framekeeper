# Slice 0115 - Packs Define Implementation Defaults

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

Add an episode page about packs defining implementation defaults.

## In Scope

- create one episode page about the role of packs
- link it to the concept and note pages that support pack selection

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why packs define defaults

## Main Business Rules

- packs define defaults
- the pack should be explicit
- the page should not become a core MRL description

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/046-packs-define-implementation-defaults.md` exists
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
- the page reinforces pack defaults
- the change is represented in `work/changes/0027/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a starter-pack overview
