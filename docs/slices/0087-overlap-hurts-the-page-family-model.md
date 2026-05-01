# Slice 0087 - Overlap Hurts The Page Family Model

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

Add a concept page about overlap hurting the page-family model.

## In Scope

- create one concept page about overlap and page-family boundaries

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why repeated ideas blur the model

## Main Business Rules

- page families should stay distinct
- overlap should not erase the boundary between families
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/overlap-hurts-the-page-family-model.md` exists
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
- the page reinforces family boundaries
- the change is represented in `work/changes/0021/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a taxonomy note
