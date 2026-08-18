from pipeline_copilot.llm.base import BaseLLM
from pipeline_copilot.rag.prompt_builder import PromptBuilder
from pipeline_copilot.rag.retriever import KnowledgeRetriever


class PipelineCopilot:

    def __init__(
        self,
        retriever: KnowledgeRetriever,
        llm_service: BaseLLM,
        prompt_builder: PromptBuilder,
    ):
        self.retriever = retriever
        self.llm_service = llm_service
        self.prompt_builder = prompt_builder

    def ask(
        self,
        question: str,
        top_k: int = 3,
    ) -> str:

        results = self.retriever.retrieve(
            question,
            top_k=top_k,
        )

        chunks = [
            result["chunk"]
            for result in results
        ]

        prompt = self.prompt_builder.build(
            question,
            chunks,
        )

        return self.llm_service.generate(prompt)