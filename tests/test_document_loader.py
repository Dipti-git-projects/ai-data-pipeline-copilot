from pathlib import Path

from pipeline_copilot.rag.document_loader import DocumentLoader


def test_load_documents():

    loader = DocumentLoader()

    documents = loader.load_directory(
        Path("data/knowledge")
    )

    assert len(documents) == 2