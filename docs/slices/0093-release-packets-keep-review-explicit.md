# Slice 0093 - Release Packets Keep Review Explicit

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

Add a concept page about release packets keeping review explicit.

## In Scope

- create one concept page about release packets and explicit review

## Use-Case Contract

- input: manually authored concept content
- output: one structured concept page under `docs/concepts/`
- behavior: the page should explain why the review surface should stay visible

## Main Business Rules

- release review should stay explicit
- the packet should gather useful output
- the page should stay short and reusable

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/concepts/release-packets-keep-review-explicit.md` exists
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
- the page reinforces explicit review
- the change is represented in `work/changes/0022/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into a systems design note
