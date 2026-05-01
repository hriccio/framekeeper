# Slice 0041 - Notes Are For Intermediate Thinking

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

Add an episode page that says notes are for intermediate thinking.

## In Scope

- create one episode page about the role of notes
- link it to the note and concept pages that motivate it

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should explain what notes are for

## Main Business Rules

- notes can capture intermediate thoughts
- notes should stay separate from raw transcripts
- the page should not become a notebook dump

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/017-notes-are-for-intermediate-thinking.md` exists
- the home page links to the page
- the episodes index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the episodes index lists the page

## Scenario Definition

1. open the episode page
2. follow links to the supporting note and concept pages

## Done Criteria

- the episode page exists and is linked
- the page reinforces the role of notes
- the change is represented in `work/changes/0012/implementation.md`

## Resolved Design Decisions

- keep the page focused on note usage
- avoid broadening it into a drafting process guide

