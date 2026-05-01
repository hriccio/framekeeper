# Slice 0037 - Version History Is Visible

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

Add a concept page that says version history should remain visible in the site.

## In Scope

- create one concept page about version history
- link it to the episode and note pages that motivate it

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why version history matters

## Main Business Rules

- version history should be visible where it helps readers
- updates should not erase prior context
- the page should not become a Git tutorial

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/version-history-is-visible.md` exists
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
- the page preserves the visibility of version history
- the change is represented in `work/changes/0011/implementation.md`

## Resolved Design Decisions

- keep the page about readability, not tooling
- avoid introducing change-log formatting into the concept page

