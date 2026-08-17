from pipeline_copilot.db.repository import PipelineRunRepository
from pipeline_copilot.models import PipelineInvestigationRequest


def test_find_runs_by_pipeline():

    request = PipelineInvestigationRequest(
        pipeline_name="CUSTOMER_INCREMENTAL_LOAD"
    )

    repository = PipelineRunRepository()

    runs = repository.find_runs_by_pipeline(request)

    assert len(runs) >= 1