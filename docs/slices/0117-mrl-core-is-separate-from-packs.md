# Slice 0117 - MRL Core Is Separate From Packs

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

Add a concept page about MRL core being separate from packs.

## In Scope

- create one concept page about the separation between MRL core and packs

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why the loop is not the pack

## Main Business Rules

- MRL core stays architecture-agnostic
- packs provide implementation defaults
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/mrl-core-is-separate-from-packs.md` exists
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
- the page reinforces core/pack separation
- the change is represented in `work/changes/0027/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a pack manifesto
