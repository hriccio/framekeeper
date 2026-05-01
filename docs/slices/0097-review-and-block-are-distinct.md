# Slice 0097 - Review And Block Are Distinct

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

Add a concept page about review and block being distinct.

## In Scope

- create one concept page about the distinction between review and block

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why the two states must stay separate

## Main Business Rules

- review is a checkpoint
- block is a stop
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/review-and-block-are-distinct.md` exists
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
- the page reinforces the state distinction
- the change is represented in `work/changes/0023/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a process taxonomy
