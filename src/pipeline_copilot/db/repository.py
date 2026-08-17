from pipeline_copilot.db.connection import get_connection
from pipeline_copilot.models import (
    PipelineInvestigationRequest,
    PipelineRun,
)


class PipelineRunRepository:

    def find_runs_by_pipeline(
        self,
        request: PipelineInvestigationRequest,
    ) -> list[PipelineRun]:

        connection = get_connection()

        try:
            cursor = connection.execute(
                """
                SELECT
                    run_id,
                    pipeline_name,
                    start_time,
                    end_time,
                    status,
                    error_message,
                    records_processed
                FROM pipeline_run_log
                WHERE pipeline_name = ?
                ORDER BY start_time DESC
                """,
                (request.pipeline_name,),
            )

            rows = cursor.fetchall()

            return [
                PipelineRun(
                    run_id=row[0],
                    pipeline_name=row[1],
                    start_time=row[2],
                    end_time=row[3],
                    status=row[4],
                    error_message=row[5],
                    records_processed=row[6],
                )
                for row in rows
            ]

        finally:
            connection.close()