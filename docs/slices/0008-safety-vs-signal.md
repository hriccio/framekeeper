# Slice 0008 - Safety Vs Signal

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

Add a concept page that keeps the hard safety gate separate from the soft
signal layer.

## In Scope

- create one concept page about safety versus signal
- link it back to the safety episode page and the processing slice

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the concept should state that signal never blocks

## Main Business Rules

- safety is a hard constraint
- signal is diagnostic only
- the concept page should not treat quality as policy enforcement

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/safety-vs-signal.md` exists
- the home page links to the page
- the concepts index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the concepts index lists the page

## Scenario Definition

1. open the concept page
2. follow links to the episode pages that refer to it

## Done Criteria

- the concept page exists and is linked
- the page preserves the safety/signal boundary
- the change is represented in `work/changes/0005/implementation.md`

## Resolved Design Decisions

- keep the page narrow and boundary-focused
- avoid introducing scoring language that implies blocking power

