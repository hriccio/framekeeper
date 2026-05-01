# Slice 0018 - YouTube Community Guidelines Reference

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

Add a reference page for the YouTube policy source that motivates the
knowledge-layer safety boundary.

## In Scope

- create one reference page for YouTube community guidelines
- link it to the episodes and concepts that depend on it

## Use-Case Contract

- input: manually authored reference content
- output: one structured reference page under `docs/references/`
- behavior: the page should point to the policy source without overexplaining it

## Main Business Rules

- references should remain concise
- policy sources should be easy to find
- the reference page should not re-host the policy text

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/references/youtube-community-guidelines.md` exists
- the home page links to the page
- the references index lists the page

## Initial Test Plan

- a test verifies the page exists
- a test verifies the home page links to the page
- a test verifies the references index lists the page

## Scenario Definition

1. open the reference page
2. follow links from the episodes and concept pages that cite it

## Done Criteria

- the reference page exists and is linked
- the page gives a clear policy source entry point
- the change is represented in `work/changes/0007/implementation.md`

## Resolved Design Decisions

- keep the page concise and source-oriented
- avoid copying policy text into the site

