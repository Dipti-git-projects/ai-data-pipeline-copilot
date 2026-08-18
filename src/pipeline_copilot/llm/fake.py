from pipeline_copilot.llm.base import BaseLLM


class FakeLLM(BaseLLM):

    def generate(self, prompt: str) -> str:
        return "This is a test response."