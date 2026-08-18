from pipeline_copilot.models import (
    DocumentChunk,
    KnowledgeDocument,
)


class DocumentChunker:

    def chunk_document(
        self,
        document: KnowledgeDocument,
        chunk_size: int = 500,
    ) -> list[DocumentChunk]:

        content = document.content

        chunks = []

        for index in range(
            0,
            len(content),
            chunk_size,
        ):

            chunk_content = content[
                index:index + chunk_size
            ]

            chunks.append(
                DocumentChunk(
                    chunk_id=f"{document.document_id}-{index}",
                    document_id=document.document_id,
                    content=chunk_content,
                    metadata={
                        "source": document.source,
                        "title": document.title,
                    },
                )
            )

        return chunks