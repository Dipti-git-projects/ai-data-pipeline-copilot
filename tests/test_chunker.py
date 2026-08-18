from pipeline_copilot.rag.chunker import DocumentChunker


def test_chunker_preserves_section_metadata():

    content = """
# Snowflake Connection Troubleshooting

## Common Causes

Network connectivity problems can cause
Snowflake connection failures.

## Recovery

Retry the pipeline after confirming
the connection is available.
"""

    chunker = DocumentChunker(
        chunk_size=500,
        overlap=50,
    )

    chunks = chunker.chunk(
        document_id="snowflake-runbook",
        content=content,
        metadata={
            "source": "snowflake_connection.md",
            "document_type": "runbook",
        },
    )

    assert len(chunks) > 0

    assert chunks[0].metadata["source"] == (
        "snowflake_connection.md"
    )

    assert chunks[0].metadata["document_type"] == (
        "runbook"
    )

    assert "section" in chunks[0].metadata