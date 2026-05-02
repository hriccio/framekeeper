# Slice 0143 - Evidence Weight Shapes Content Form

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

Add a concept page about evidence weight shaping content form.

## In Scope

- create one concept page about evidence-heavy vs explanation-heavy material
- connect it to the classification episode pages

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain how evidence weight shapes content form

## Main Business Rules

- source-heavy material prefers references
- explanatory material prefers concepts
- story-like material prefers episodes

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/059-evidence-weight-shapes-content-form.md` exists
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
- the page explains how evidence weight changes content form
- the change is represented in `work/changes/0032/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid making it sound like a generic content rubric
