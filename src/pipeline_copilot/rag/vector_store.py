import faiss
import numpy as np

from pipeline_copilot.models import DocumentChunk


class VectorStore:

    def __init__(self, dimension: int):

        self.index = faiss.IndexFlatIP(dimension)

        self.chunks: list[DocumentChunk] = []

    def add(
        self,
        chunks: list[DocumentChunk],
        embeddings,
    ):

        vectors = np.asarray(
            embeddings,
            dtype="float32",
        )

        self.index.add(vectors)

        self.chunks.extend(chunks)

    def search(
        self,
        query_embedding,
        top_k: int = 3,
    ):

        query_vector = np.asarray(
            [query_embedding],
            dtype="float32",
        )

        scores, indices = self.index.search(
            query_vector,
            top_k,
        )

        results = []

        for score, index in zip(
            scores[0],
            indices[0],
        ):

            if index == -1:
                continue

            results.append(
                {
                    "chunk": self.chunks[index],
                    "score": float(score),
                }
            )

        return results