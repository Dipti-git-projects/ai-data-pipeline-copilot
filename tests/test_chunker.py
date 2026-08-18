from pipeline_copilot.models import KnowledgeDocument
from pipeline_copilot.rag.chunker import DocumentChunker


def test_document_is_chunked():

    document = KnowledgeDocument(
        document_id="test",
        title="Test Document",
        content="A" * 1200,
        source="test.md",
    )

    chunker = DocumentChunker()

    chunks = chunker.chunk_document(
        document,
        chunk_size=500,
    )

    assert len(chunks) == 3