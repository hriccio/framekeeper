# Slice 0096 - Block Means Stop

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

Add an episode page about block meaning stop.

## In Scope

- create one episode page about the block state
- link it to the concept and note pages that support the safety tier model

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain why block is a hard stop

## Main Business Rules

- block is a stop state
- blocked content does not continue automatically
- the page should not become an operations manual

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/039-block-means-stop.md` exists
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
- the page reinforces block as a stop
- the change is represented in `work/changes/0023/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid turning it into an incident response playbook
