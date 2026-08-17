from pipeline_copilot.db.repository import PipelineRunRepository
from pipeline_copilot.models import PipelineInvestigationRequest
from pipeline_copilot.services.pipeline_analysis import (
    PipelineAnalysisService,
)


def test_common_errors():

    request = PipelineInvestigationRequest(
        pipeline_name="CUSTOMER_INCREMENTAL_LOAD"
    )

    service = PipelineAnalysisService(
        PipelineRunRepository()
    )

    errors = service.find_common_errors(request)

    assert errors["Snowflake connection timeout"] == 2