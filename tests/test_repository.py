from pipeline_copilot.db.repository import PipelineRunRepository
from pipeline_copilot.models import PipelineInvestigationRequest


def test_find_runs_by_pipeline(test_connection):

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
                "2026-08-15 08:10:00",
                "SUCCESS",
                None,
                1000,
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

    repository = PipelineRunRepository(test_connection)

    request = PipelineInvestigationRequest(
        pipeline_name="CUSTOMER_INCREMENTAL_LOAD"
    )

    runs = repository.find_runs_by_pipeline(request)

    assert len(runs) == 2
    assert runs[0].run_id == "TEST002"
    assert runs[1].run_id == "TEST001"