# GitHub Pages Knowledge Layer — Codex Handoff

## Context

I started a YouTube channel called **@umoutrohenrique**, where I talk in Portuguese about software development and AI.

The channel is conversational: I record videos thinking out loud, exploring ideas, reacting to software/AI trends, and clarifying what I believe or do not believe about development with AI.

I now want a second layer for this content: a slower, structured place where the knowledge extracted from each video can be consumed at another pace.

The intended flow is:

```text
video -> transcript -> extract important ideas -> enrich with references -> publish as structured markdown/site content
```

The goal is not only to publish articles. The goal is to build a **source of truth** for the ideas that emerge from the channel.

---

## Decision

Use **GitHub Pages** with **no custom domain** for now.

Do not block the project on domain registration, `.dev` availability, branding, DNS, HTTPS setup, or external hosting decisions.

Initial hosting target:

```text
https://<github-username>.github.io/<repo-name>/
```

This keeps the system simple, versioned, markdown-native, and compatible with Codex-assisted workflows.

---

## Why not WastingNoTime or CodingZen?

This content does **not** currently fit cleanly into:

- `wastingnotime.org`
- `codingzen.org`

### WastingNoTime

WNT should remain more curated, refined, and structurally clean.

The YouTube knowledge layer is more temporal and exploratory. It represents thinking in motion, not only finished conclusions.

Forcing this content into WNT could weaken WNT's coherence.

### CodingZen

CodingZen is more about exploration, creative coding, games, visualization, and playful technical practice.

The YouTube channel is broader: software development, AI, personal reasoning, development culture, methods, and context.

So this new layer should be separate.

---

## Purpose of the new site

This is not just a blog.

It is a **public knowledge layer** for @umoutrohenrique.

Primary purposes:

1. Store refined ideas extracted from videos.
2. Preserve references and source links.
3. Allow slower consumption than YouTube.
4. Create a durable source of truth for recurring concepts.
5. Support future automation from transcript to structured content.
6. Keep exploratory content separate from WNT and CodingZen.

---

## Content model

Each video should be processed into one or more markdown artifacts.

### Main artifact types

```text
/episodes
/concepts
/references
/notes
```

### episodes

One page per YouTube video.

Purpose: preserve the structured version of what was said in a specific video.

Example:

```text
/episodes/001-ai-nao-e-nova.md
/episodes/002-contexto-em-ia.md
/episodes/003-o-que-nao-vou-fazer-no-canal.md
```

### concepts

Reusable ideas that appear across multiple videos.

Examples:

```text
/concepts/contexto-em-ia.md
/concepts/spec-driven-development.md
/concepts/model-refinement-lab.md
/concepts/ia-no-desenvolvimento.md
```

### references

Curated external references used to enrich videos and concepts.

Examples:

```text
/references/fabio-akita.md
/references/machine-learning.md
/references/spec-driven-development.md
```

### notes

Optional raw or semi-refined notes.

This can be used as an intermediate staging area before publishing refined content.

---

## Recommended repository shape

```text
.
├── README.md
├── docs/
│   ├── index.md
│   ├── episodes/
│   │   └── 001-template.md
│   ├── concepts/
│   │   └── index.md
│   ├── references/
│   │   └── index.md
│   └── notes/
│       └── index.md
├── transcripts/
│   └── raw/
├── work/
│   └── drafts/
└── .github/
    └── workflows/
        └── pages.yml
```

### Important note

Use `docs/` as the GitHub Pages publishing root if using the simple GitHub Pages configuration.

Keep raw transcripts outside the published site unless intentionally exposed.

---

## Markdown template for an episode

```markdown
# <Episode Title>

## Metadata

- YouTube channel: @umoutrohenrique
- Video URL: <url>
- Published date: <yyyy-mm-dd>
- Source transcript: <path or note>
- Status: draft | refined | published

---

## Core idea

Short summary of the main point of the video.

---

## What I said

Structured reconstruction of the main reasoning from the video.

Use sections, not raw transcript paragraphs.

---

## Key points

- Point 1
- Point 2
- Point 3

---

## Concepts mentioned

- [[concept-1]]
- [[concept-2]]

---

## References

- Reference title — URL
- Reference title — URL

---

## Refined conclusion

What remains after processing the video.

This does not need to be exactly what was said. It should capture what became clearer after reviewing the transcript.

---

## Follow-up ideas

- Possible future video
- Possible concept page
- Open question
```

---

## Transcript processing workflow

For each video:

1. Save transcript in `transcripts/raw/`.
2. Generate a draft in `work/drafts/`.
3. Extract:
   - main idea
   - key arguments
   - reusable concepts
   - references needed
   - possible follow-up questions
4. Enrich with external references.
5. Create or update related concept pages.
6. Move refined episode markdown to `docs/episodes/`.
7. Update `docs/index.md` and `docs/episodes/index.md`.

---

## First implementation slice

Codex should implement only the minimal useful system first.

### Slice 1 goal

Create a GitHub Pages-ready markdown site with:

- home page
- episodes index
- concepts index
- references index
- one episode template
- basic navigation
- clear folder structure

### Avoid in slice 1

Do not implement complex automation yet.

Avoid:

- custom domain
- CMS
- database
- search engine
- heavy theme customization
- transcript AI automation
- complex static-site generator decisions unless already needed

The first slice should make it easy to manually add markdown pages and publish them through GitHub Pages.

---

## Suggested homepage copy

```markdown
# Um Outro Henrique — Knowledge Layer

This is the structured knowledge layer behind the YouTube channel @umoutrohenrique.

The videos are where ideas are explored out loud.
This site is where those ideas are extracted, refined, referenced, and preserved.

## Sections

- [Episodes](./episodes/)
- [Concepts](./concepts/)
- [References](./references/)
```

---

## Guiding principles

1. **Markdown first**
   - Markdown is the source of truth.

2. **No custom domain for now**
   - Use GitHub Pages default URL.

3. **Do not overdesign**
   - Validate the publishing rhythm before adding tooling.

4. **Separate raw from refined**
   - Raw transcripts are input, not final content.

5. **Keep WNT and CodingZen clean**
   - This site is its own personal knowledge layer.

6. **Use videos as signal, not final text**
   - The transcript should be processed, not pasted.

7. **Prefer continuity over optimization**
   - The system should be easy to maintain after every video.

---

## Future automation ideas

After the manual system works, possible automation:

1. Pull transcript from YouTube.
2. Generate draft episode markdown.
3. Suggest concepts to create/update.
4. Suggest references to enrich the content.
5. Produce metadata:
   - title
   - description
   - tags
   - concepts
   - status
6. Open a pull request with generated content.

Automation should come after the structure proves useful manually.

---

## Done criteria for Codex

The first implementation is done when:

- GitHub Pages can serve the site from `docs/`.
- `docs/index.md` exists.
- `docs/episodes/index.md` exists.
- `docs/concepts/index.md` exists.
- `docs/references/index.md` exists.
- `docs/episodes/001-template.md` exists.
- Navigation links work locally in markdown.
- README explains how to publish through GitHub Pages.

---

## Non-goals

This is not:

- WastingNoTime
- CodingZen
- a polished publication platform
- a newsletter
- a commercial product
- a CMS project
- a domain/branding project

This is a lightweight source-of-truth layer for ideas generated through @umoutrohenrique.
