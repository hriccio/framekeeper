# Request Slice Map

- Change: `0001`
- Request: `work/changes/0001/request.md`
- Status: accepted

## Request Boundary

Implement the first executable transcript-processing boundary for Framekeeper:
safety classification must decide the pipeline, signal feedback must remain
non-blocking, and the resulting release packet must be human-readable.

## Slice Mapping

| Slice | Status | Request coverage | Acceptance evidence |
| --- | --- | --- | --- |
| `docs/slices/0001-video-processing-classification.md` | accepted | Covers the entire request with one transcript-processing slice, including safety classification, release packet assembly, and non-blocking signal feedback. | `tests/unit/test_process_video_transcript.py`, `work/changes/0001/implementation.md` |

## Out Of Scope

- raw video ingestion and transcription
- storage persistence
- GitHub Pages publishing
- automatic upload or publication
- external model or API dependencies

## Open Questions

- none for this slice

## EGD Notes

Expectation-gap review should verify that safety, not signal, is the pipeline
gate; that `BLOCK` skips signal generation; and that `REVIEW` still produces a
manual-confirmation packet.

