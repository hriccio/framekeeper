# Slice 0123 - Deterministic Packets Keep Evidence Reviewable

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

Add a concept page explaining why deterministic packets keep evaluation
evidence reviewable.

## In Scope

- create one concept page about compact evidence packets
- connect it to the episode pages that describe the evaluation loop

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should describe how packet shape supports review

## Main Business Rules

- packets should be compact
- packets should preserve enough context to review later
- raw dumps are not a good review artifact

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/051-deterministic-packets-keep-evidence-reviewable.md` exists
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
- the page explains why compact packets are easier to review
- the change is represented in `work/changes/0028/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid treating packets as raw archives
