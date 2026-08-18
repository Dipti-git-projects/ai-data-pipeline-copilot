from pipeline_copilot.models import DocumentChunk


class PromptBuilder:

    def build(
        self,
        question: str,
        chunks: list[DocumentChunk],
    ) -> str:

        context_parts = []

        for chunk in chunks:

            source = chunk.metadata.get(
                "source",
                "Unknown source",
            )

            section = chunk.metadata.get(
                "section",
                "Unknown section",
            )

            context_parts.append(
                f"""
SOURCE: {source}
SECTION: {section}

CONTENT:
{chunk.content}
"""
            )

        context = "\n\n".join(context_parts)

        return f"""
You are an AI Data Pipeline Copilot.

Answer the user's question using ONLY the
provided organizational context.

Do not invent information.

If the context does not contain enough
information to answer the question, say:

"Insufficient information in the available
knowledge base."

USER QUESTION:
{question}

ORGANIZATIONAL CONTEXT:
{context}

Provide:

1. Likely cause
2. Evidence
3. Recommended action
4. Sources used

Keep the response concise and practical.
"""