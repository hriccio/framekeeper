# Slice 0120 - Scenario Evaluation Is Not Tests

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

Add an episode page explaining that scenario evaluation complements tests
rather than replacing them.

## In Scope

- create one episode page about the purpose of scenario evaluation
- link it to the concept and note pages that support evaluation review

## Use-Case Contract

- input: manually authored episode content
- output: one structured episode page under `docs/episodes/`
- behavior: the page should distinguish evaluation review from correctness tests

## Main Business Rules

- scenario evaluation is not the test suite
- expectation gaps are review questions
- evaluation should not claim final truth

## Required Ports

- none

## Out Of Scope

- transcript automation
- publishing automation
- content generation automation

## Candidate Acceptance Criteria

- `docs/episodes/048-scenario-evaluation-is-not-tests.md` exists
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
- the page separates scenario evaluation from tests
- the change is represented in `work/changes/0028/implementation.md`

## Resolved Design Decisions

- keep the page concise
- avoid collapsing review into test execution
