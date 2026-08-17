import pytest
from pydantic import ValidationError

from pipeline_copilot.models import PipelineInvestigationRequest


def test_valid_pipeline_request():
    request = PipelineInvestigationRequest(
        pipeline_name="CUSTOMER_INCREMENTAL_LOAD"
    )

    assert request.pipeline_name == "CUSTOMER_INCREMENTAL_LOAD"


def test_empty_pipeline_name_is_invalid():
    with pytest.raises(ValidationError):
        PipelineInvestigationRequest(
            pipeline_name=""
        )