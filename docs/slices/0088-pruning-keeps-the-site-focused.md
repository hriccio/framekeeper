# Slice 0088 - Pruning Keeps The Site Focused

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

Add a concept page about pruning keeping the site focused.

## In Scope

- create one concept page about pruning and editorial focus

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why pruning preserves one clear purpose

## Main Business Rules

- pruning should preserve focus
- the distinct version should stay visible
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/pruning-keeps-the-site-focused.md` exists
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
- the page reinforces pruning as focus preservation
- the change is represented in `work/changes/0021/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into an archival policy
