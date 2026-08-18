# from pipeline_copilot.models import (
#     DocumentChunk,
#     KnowledgeDocument,
# )


# class DocumentChunker:

#     def chunk_document(
#         self,
#         document: KnowledgeDocument,
#         chunk_size: int = 500,
#     ) -> list[DocumentChunk]:

#         content = document.content

#         chunks = []

#         for index in range(
#             0,
#             len(content),
#             chunk_size,
#         ):

#             chunk_content = content[
#                 index:index + chunk_size
#             ]

#             chunks.append(
#                 DocumentChunk(
#                     chunk_id=f"{document.document_id}-{index}",
#                     document_id=document.document_id,
#                     content=chunk_content,
#                     metadata={
#                         "source": document.source,
#                         "title": document.title,
#                     },
#                 )
#             )

#         return chunks

import re

from pipeline_copilot.models import DocumentChunk


class DocumentChunker:

    def __init__(
        self,
        chunk_size: int = 500,
        overlap: int = 50,
    ):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def chunk(
        self,
        document_id: str,
        content: str,
        metadata: dict | None = None,
    ) -> list[DocumentChunk]:

        metadata = metadata or {}

        sections = re.split(
            r"(?m)^## ",
            content,
        )

        chunks = []

        for index, section in enumerate(sections):

            section = section.strip()

            if not section:
                continue

            lines = section.splitlines()

            if lines:

                section_name = lines[0].strip()

                section_content = "\n".join(
                    lines[1:]
                ).strip()

            else:
                section_name = "Unknown"

                section_content = section

            for start in range(
                0,
                len(section_content),
                self.chunk_size - self.overlap,
            ):

                chunk_text = section_content[
                    start:start + self.chunk_size
                ]

                if not chunk_text:
                    continue

                chunk_metadata = {
                    **metadata,
                    "section": section_name,
                }

                chunks.append(
                    DocumentChunk(
                        chunk_id=f"{document_id}-{index}-{start}",
                        document_id=document_id,
                        content=chunk_text,
                        metadata=chunk_metadata,
                    )
                )

        return chunks