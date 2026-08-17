from pipeline_copilot.db.repository import PipelineRunRepository
from pipeline_copilot.models import (
    PipelineInvestigationRequest,
    PipelineRun,
    PipelineStatus,
)


class PipelineAnalysisService:

    def __init__(self, repository: PipelineRunRepository):
        self.repository = repository

    def get_failed_runs(
        self,
        request: PipelineInvestigationRequest,
    ) -> list[PipelineRun]:

        runs = self.repository.find_runs_by_pipeline(request)

        return [
            run
            for run in runs
            if run.status == PipelineStatus.FAILED
        ]

    def find_common_errors(
        self,
        request: PipelineInvestigationRequest,
    ) -> dict[str, int]:

        failed_runs = self.get_failed_runs(request)

        error_counts: dict[str, int] = {}

        for run in failed_runs:
            if run.error_message:
             error_counts[run.error_message] = (
                error_counts.get(run.error_message, 0) + 1
            )

        return error_counts