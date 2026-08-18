from pipeline_copilot.db.repository import PipelineRunRepository
from pipeline_copilot.models import PipelineInvestigationRequest
from pipeline_copilot.services.pipeline_analysis import (
    PipelineAnalysisService,
)


def test_common_errors(test_connection):

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
            (
                "TEST003",
                "CUSTOMER_INCREMENTAL_LOAD",
                "2026-08-17 08:00:00",
                "2026-08-17 08:20:00",
                "SUCCESS",
                None,
                5000,
            ),
        ],
    )

    repository = PipelineRunRepository(test_connection)

    service = PipelineAnalysisService(repository)

    request = PipelineInvestigationRequest(
        pipeline_name="CUSTOMER_INCREMENTAL_LOAD"
    )

    errors = service.find_common_errors(request)

    assert errors["Snowflake connection timeout"] == 2