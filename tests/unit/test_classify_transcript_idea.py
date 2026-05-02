from __future__ import annotations

from pathlib import Path

from app.application.classify_transcript_idea import ClassifyTranscriptIdea
from app.domain.content_classification import ContentFamily
from app.domain.models import Transcript, VideoSubmission


def test_source_heavy_transcript_maps_to_reference() -> None:
    submission = VideoSubmission(
        video_id="video-reference",
        title="Community guidelines and sources",
        transcript=Transcript(
            "This walkthrough points to the official documentation and the community "
            "guidelines so the source stays easy to find."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.REFERENCE
    assert result.recommendation.matched_cue == "community guidelines"
    assert "source" in result.recommendation.reason


def test_workflow_language_maps_to_note() -> None:
    submission = VideoSubmission(
        video_id="video-note",
        title="Publishing checklist",
        transcript=Transcript(
            "This is the workflow checklist for turning the transcript into a draft."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.NOTE
    assert result.recommendation.matched_cue == "workflow"
    assert "notes" in result.recommendation.reason


def test_explanatory_language_maps_to_concept() -> None:
    submission = VideoSubmission(
        video_id="video-concept",
        title="Thinking about boundaries",
        transcript=Transcript(
            "The principle here is the boundary between what we keep and what we drop."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.CONCEPT
    assert result.recommendation.matched_cue == "principle"
    assert "concepts" in result.recommendation.reason


def test_generic_story_defaults_to_episode() -> None:
    submission = VideoSubmission(
        video_id="video-episode",
        title="Talking through context",
        transcript=Transcript(
            "Today I am talking through a practical example of context in software."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.EPISODE
    assert result.recommendation.matched_cue == "default"


def test_portuguese_reflective_transcript_defaults_to_episode() -> None:
    submission = VideoSubmission(
        video_id="video-portuguese-episode",
        title="Eu tenho pensado sobre desenvolvimento de software",
        transcript=Transcript(
            "Tem muita coisa que eu faço manualmente, mas isso não quer dizer que "
            "o vídeo seja uma explicação geral."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.EPISODE
    assert result.recommendation.matched_cue == "default"


def test_portuguese_workflow_language_maps_to_note() -> None:
    submission = VideoSubmission(
        video_id="video-portuguese-note",
        title="Fluxo de publicação",
        transcript=Transcript(
            "Este é o passo a passo para transformar a transcrição em nota."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.NOTE
    assert result.recommendation.matched_cue == "passo a passo"


def test_portuguese_reference_language_maps_to_reference() -> None:
    submission = VideoSubmission(
        video_id="video-portuguese-reference",
        title="Fonte oficial",
        transcript=Transcript(
            "Segundo a documentação oficial, a referência principal fica aqui."
        ),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.REFERENCE
    assert result.recommendation.matched_cue == "documentacao"


def test_real_portuguese_transcript_defaults_to_episode() -> None:
    transcript_path = Path(
        "/home/henrique/Documents/40_projects/um_outro_henrique/transcripts/"
        "Um outro Henrique - eu tenho pensado sobre desenvolvimento de software [00].srt"
    )
    transcript_text = transcript_path.read_text(encoding="utf-8")

    submission = VideoSubmission(
        video_id="real-001",
        title="Um outro Henrique - eu tenho pensado sobre desenvolvimento de software",
        transcript=Transcript(transcript_text),
    )

    result = ClassifyTranscriptIdea().execute(submission)

    assert result.recommendation.family is ContentFamily.EPISODE
    assert result.recommendation.matched_cue == "default"
