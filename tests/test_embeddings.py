from pipeline_copilot.rag.embedding_service import EmbeddingService


def test_embedding_generation():

    service = EmbeddingService()

    embeddings = service.embed(
        [
            "Snowflake connection timeout",
            "Pipeline could not connect to Snowflake",
        ]
    )

    assert len(embeddings) == 2
    assert embeddings.shape[1] > 0