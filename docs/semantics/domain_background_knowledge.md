# Domain Background Knowledge

## Channel Context

`@umoutrohenrique` is a Portuguese YouTube channel about software development,
AI, development culture, personal reasoning, methods, and context.

The channel is conversational and exploratory. Videos capture thinking in
motion, not polished final doctrine.

## Automation Context

The system should reduce operational friction from recording to review without
making the channel performative.

The source context defines three stages:

- recording: Henrique records naturally
- processing: automation transcribes, checks safety, and produces feedback
- release: Henrique decides what becomes public

## Safety Context

YouTube policy risk is a hard constraint. The safety gate exists to reduce risk
around areas such as:

- spam or deceptive practices
- misleading or scam content
- harmful or dangerous behavior
- hate speech or harassment
- misinformation with real-world harm
- copyright issues

Risk levels:

- `SAFE`: continue pipeline
- `REVIEW`: require manual confirmation
- `BLOCK`: stop pipeline

The exact policy reference should be refreshed from official YouTube/Google
sources during implementation because platform rules can change.

## Signal Context

Signal feedback is soft and diagnostic. It can include:

- one-sentence summary
- likely audience
- hook
- clarity score
- specificity score
- coherence score
- novelty score

These outputs exist to help review, not to rank, suppress, or optimize videos.

## Knowledge-Layer Context

The broader content system also needs a slower public knowledge layer using
GitHub Pages.

Intended flow:

```text
video -> transcript -> extract important ideas -> enrich with references -> publish structured markdown/site content
```

Recommended artifact types:

- `episodes`
- `concepts`
- `references`
- `notes`

Raw transcripts should remain outside the public site unless intentionally
exposed.

## Evaluation Risks

Watch for these expectation gaps:

- accidentally treating quality or novelty as a publication gate
- mixing safety classification with signal scoring
- building automatic publishing before manual release review exists
- overfitting to YouTube algorithm behavior
- storing important business truth only in generated HTML
- allowing raw transcripts to become public by default
- making external LLM or transcription services hard dependencies too early
