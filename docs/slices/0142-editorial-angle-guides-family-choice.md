# Slice 0142 - Editorial Angle Guides Family Choice

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

Add a concept page about editorial angle guiding page family choice.

## In Scope

- create one concept page about the angle as a classification cue
- connect it to the episode pages that motivate the choice

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain how editorial angle guides family choice

## Main Business Rules

- story-like material tends toward episodes
- principle-like material tends toward concepts
- source-heavy material tends toward references

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/058-editorial-angle-guides-family-choice.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related episode and note pages

## Done Criteria

- the concept page exists and is linked
- the page explains how angle guides family choice
- the change is represented in `work/changes/0032/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making family choice into a rigid taxonomy
