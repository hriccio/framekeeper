# 🎥 um_outro_henrique — Content Automation System (MRL Context)

---

## 1. 🎯 Objective

Design a **low-friction, high-coherence content pipeline** for the YouTube channel:

* Preserve Henrique’s **authentic thinking style**
* Reduce operational friction (record → publish)
* Protect the channel from **policy risk**
* Avoid degrading long-term **signal quality**

This system must **assist**, not replace, human judgment.

---

## 2. 🧭 Core Principles (Non-Negotiable)

### 2.1 Automation Boundary

> Automation handles **mechanics**
> Henrique handles **meaning**

---

### 2.2 Safety vs Signal Separation

The system MUST separate:

* **Safety (hard constraint)**
* **Signal (soft feedback)**

Never mix both.

---

### 2.3 No Performance Optimization

The system must NOT:

* block videos based on “quality”
* optimize for algorithmic patterns
* bias toward safe/generic content

> The channel is exploratory, not performative.

---

### 2.4 Human Final Authority

Only Henrique decides:

* what gets published
* when it becomes public
* what represents his thinking

---

## 3. 🏗️ Pipeline Overview

```
1. Recording
2. Processing (automated)
3. Release (manual)
```

---

## 4. 🎥 Stage 1 — Recording

### Description

Henrique records video naturally.

### Constraints

* No scripting required
* One core idea per video
* Avoid re-record loops

### Output

```
/videos/raw/{timestamp}.mp4
```

---

## 5. ⚙️ Stage 2 — Processing (Automated)

---

### 5.1 Transcription

#### Tooling

* Whisper (local or API)

#### Output

```
/videos/processed/{id}/transcript.txt
```

---

### 5.2 🛡️ Safety Gate (Hard Check)

This is the ONLY stage that can block a video.

---

### Purpose

Prevent violations of YouTube policies.

---

### Context

YouTube enforces rules against:

* spam / deceptive practices
* misleading or scam content
* harmful or dangerous behavior
* hate speech / harassment
* misinformation with real-world harm
* copyright violations ([Google Help][1])

Violations can lead to:

* warnings
* strikes
* channel termination (3 strikes in 90 days)

---

### Input

* transcript
* generated title
* metadata

---

### Output

```
Risk Level:
- SAFE
- REVIEW
- BLOCK
```

---

### Behavior

| Level  | Action                      |
| ------ | --------------------------- |
| SAFE   | Continue pipeline           |
| REVIEW | Require manual confirmation |
| BLOCK  | Stop pipeline               |

---

### Implementation Hint

LLM classification with rules:

* detect risky claims
* detect misleading framing
* detect sensitive topics

---

## 5.3 📡 Signal Feedback (Soft — Never Blocks)

---

### Purpose

Improve clarity WITHOUT controlling output.

---

### Inputs

* transcript

---

### Outputs

#### Summary

* 1 sentence: what is the video about

#### Audience

* who benefits from this video

#### Hook

* why someone would click

---

### Heuristic Scores (optional)

```
Clarity: X/10
Specificity: X/10
Coherence: X/10
Novelty: X/10
```

⚠️ These scores are **diagnostic only**

---

### Suggestions

* improve title specificity
* highlight missing hook
* identify vague sections

---

## 5.4 🧾 Metadata Generation

---

### Outputs

```
metadata.md
```

---

### Structure

```md
# Video

## Title Options
1. ...
2. ...
3. ...

## Description
...

## Tags
...

## Summary
...

## Positioning
- reflective / technical / hybrid

## Notes
- strengths
- possible improvements
```

---

## 5.5 🔁 Future Hooks Extraction

---

### Output

```
## Next Video Ideas
- ...
- ...
- ...
```

---

### Purpose

Create continuity across videos.

---

## 5.6 📤 Upload (Private)

---

### Tooling

* YouTube Data API

---

### Behavior

* upload video
* attach metadata
* set visibility = PRIVATE

---

### Output

```
youtube_video_id
status: private
```

---

## 6. 🧭 Stage 3 — Release (Manual)

---

### Henrique Actions

* watch video once
* review metadata
* adjust title if needed
* decide publish timing

---

### Final Step

```
visibility: public
```

---

## 7. 🏗️ System Architecture

---

### Minimal Version (Recommended)

```
/videos
  /raw
  /processed
    /{video_id}
      video.mp4
      transcript.txt
      metadata.md
```

---

### Pipeline Script Responsibilities

1. detect new video
2. transcribe
3. run safety gate
4. generate signal feedback
5. generate metadata
6. upload private

---

### Tech Options

* Go (preferred, aligned with stack)
* Python (faster prototyping)

---

## 8. 🧠 Decision Rules

---

### Only 2 conditions can block a video:

1. Policy risk (Safety Gate = BLOCK)
2. Henrique does not stand by it

---

### Everything else:

→ must pass through

---

## 9. ⚖️ Anti-Corruption Rules

The system must NOT:

* auto-publish
* auto-reject based on quality
* optimize for engagement metrics
* rewrite Henrique’s voice

---

## 10. 🔥 Key Insight

This system is not a content factory.

It is:

> a **protective layer against external risk**
> without distorting internal signal

---

## 11. 🧩 Future Extensions (Optional)

* dashboard (video status tracking)
* retry queue
* thumbnail suggestion
* A/B title suggestions (manual selection only)

---

## 12. 🧭 MRL Alignment

| Phase  | Meaning in this system         |
| ------ | ------------------------------ |
| Refine | Define pipeline + rules        |
| Build  | Implement CLI + automation     |
| Expose | Run real videos through system |

---

## Final Rule

> If automation starts shaping content,
> the system is broken.

---

[1]: https://support.google.com/youtube/answer/9288567?hl=en&utm_source=chatgpt.com "YouTube's Community Guidelines"
