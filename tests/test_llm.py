from pipeline_copilot.llm.fake import FakeLLM


def test_llm_interface():

    llm = FakeLLM()

    response = llm.generate(
        "Why did the pipeline fail?"
    )

    assert response == "This is a test response."