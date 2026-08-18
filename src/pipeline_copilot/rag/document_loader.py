from pathlib import Path

from pipeline_copilot.models import KnowledgeDocument


class DocumentLoader:

    def load_directory(
        self,
        directory: Path,
    ) -> list[KnowledgeDocument]:

        documents = []

        for file_path in directory.glob("*.md"):

            content = file_path.read_text(
                encoding="utf-8"
            )

            documents.append(
                KnowledgeDocument(
                    document_id=file_path.stem,
                    title=file_path.stem.replace("_", " ").title(),
                    content=content,
                    source=str(file_path),
                )
            )

        return documents