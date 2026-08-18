from pipeline_copilot.models import DocumentChunk
from pipeline_copilot.rag.embedding_service import EmbeddingService
from pipeline_copilot.rag.retriever import KnowledgeRetriever
from pipeline_copilot.rag.vector_store import VectorStore


def test_semantic_retrieval():

    chunks = [
        DocumentChunk(
            chunk_id="1",
            document_id="snowflake",
            content="Snowflake connection timeout can occur because of network or authentication problems.",
            metadata={
                "source": "snowflake_timeout.md"
            },
        ),
        DocumentChunk(
            chunk_id="2",
            document_id="customer",
            content="Customer incremental load processes customer changes.",
            metadata={
                "source": "customer_incremental_load.md"
            },
        ),
    ]

    embedding_service = EmbeddingService()

    embeddings = embedding_service.embed(
        [chunk.content for chunk in chunks]
    )

    vector_store = VectorStore(
        dimension=embeddings.shape[1]
    )

    vector_store.add(
        chunks,
        embeddings,
    )

    retriever = KnowledgeRetriever(
        embedding_service,
        vector_store,
    )

    results = retriever.retrieve(
        "Why could the pipeline not connect to Snowflake?",
        top_k=1,
    )

    print(results)

    assert len(results) == 1

    assert (
        results[0]["chunk"].document_id
        == "snowflake"
    )