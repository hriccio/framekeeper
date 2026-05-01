# Slice 0126 - Exposure Follows Acceptance

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

Add an episode page about exposure following acceptance.

## In Scope

- create one episode page about the operational step after release
- link it to the concept and note pages that support release and exposure

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why exposure is separate from release

## Main Business Rules

- acceptance comes first
- exposure is operational
- the released state needs a portable form

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/051-exposure-follows-acceptance.md` exists
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
- the page reinforces exposure as a separate step
- the change is represented in `work/changes/0029/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid collapsing exposure into release
