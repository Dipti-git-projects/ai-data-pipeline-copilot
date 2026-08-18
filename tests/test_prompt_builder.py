from pipeline_copilot.models import DocumentChunk
from pipeline_copilot.rag.prompt_builder import PromptBuilder


def test_prompt_contains_source_metadata():

    chunk = DocumentChunk(
        chunk_id="1",
        document_id="snowflake",
        content="Snowflake connection failed.",
        metadata={
            "source": "snowflake_runbook.md",
            "section": "Troubleshooting",
        },
    )

    builder = PromptBuilder()

    prompt = builder.build(
        question="Why did the pipeline fail?",
        chunks=[chunk],
    )

    assert "snowflake_runbook.md" in prompt
    assert "Troubleshooting" in prompt
    assert "Snowflake connection failed." in prompt