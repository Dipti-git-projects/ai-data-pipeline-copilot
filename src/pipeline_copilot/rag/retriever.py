from pipeline_copilot.rag.embedding_service import EmbeddingService
from pipeline_copilot.rag.vector_store import VectorStore


class KnowledgeRetriever:

    def __init__(
        self,
        embedding_service: EmbeddingService,
        vector_store: VectorStore,
    ):
        self.embedding_service = embedding_service
        self.vector_store = vector_store

    def retrieve(
        self,
        question: str,
        top_k: int = 3,
    ):

        query_embedding = self.embedding_service.embed(
            [question]
        )[0]

        return self.vector_store.search(
            query_embedding,
            top_k=top_k,
        )