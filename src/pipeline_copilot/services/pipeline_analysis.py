from pipeline_copilot.db.repository import PipelineRunRepository
from pipeline_copilot.models import (
    FailurePattern,
    PipelineInvestigationRequest,
    PipelineRun,
    PipelineStatus,
)
#from tests.conftest import test_connection


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

    from pipeline_copilot.models import (
    FailurePattern,
    PipelineInvestigationRequest,
    PipelineStatus,
    )

    def find_failure_patterns(
        self,
        request: PipelineInvestigationRequest,
    ) -> list[FailurePattern]:

        failed_runs = self.get_failed_runs(request)

        patterns: dict[str, list[str]] = {}

        for run in failed_runs:
            if run.error_message:
                patterns.setdefault(
                run.error_message,
                [],
            ).append(run.run_id)

        return [
        FailurePattern(
            error_message=error_message,
            occurrence_count=len(run_ids),
            run_ids=run_ids,
        )
        for error_message, run_ids in patterns.items()
    ]    

    def test_failure_patterns(test_connection):

        test_connection.executemany(
        """
        INSERT INTO pipeline_run_log (
            run_id,
            pipeline_name,
            start_time,
            end_time,
            status,
            error_message,
            records_processed
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        [
            (
                "TEST001",
                "CUSTOMER_INCREMENTAL_LOAD",
                "2026-08-15 08:00:00",
                "2026-08-15 08:05:00",
                "FAILED",
                "Snowflake connection timeout",
                0,
            ),
            (
                "TEST002",
                "CUSTOMER_INCREMENTAL_LOAD",
                "2026-08-16 08:00:00",
                "2026-08-16 08:05:00",
                "FAILED",
                "Snowflake connection timeout",
                0,
            ),
        ],
    )

        service = PipelineAnalysisService(
        PipelineRunRepository(test_connection)
    )

        request = PipelineInvestigationRequest(
        pipeline_name="CUSTOMER_INCREMENTAL_LOAD"
    )

        patterns = service.find_failure_patterns(request)

        assert len(patterns) == 1
        assert patterns[0].error_message == "Snowflake connection timeout"
        assert patterns[0].occurrence_count == 2
        assert set(patterns[0].run_ids) == {"TEST001", "TEST002"}

