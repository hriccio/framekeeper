# Slice 0122 - Validation Modes Guide Slice Strategy

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

Add a concept page explaining how validation modes guide slice strategy.

## In Scope

- create one concept page about validation modes
- connect it to the evaluation pages that define the review loop

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain how validation mode shapes slice design

## Main Business Rules

- validation mode is practical guidance, not taxonomy for its own sake
- headless-first, interaction-assisted, and interaction-dependent are all valid
- the slice should make the dominant mode explicit

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/050-validation-modes-guide-slice-strategy.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the related evaluation pages

## Done Criteria

- the concept page exists and is linked
- the page explains validation mode as slice guidance
- the change is represented in `work/changes/0028/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid over-generalizing validation modes into doctrine
