from pipeline_copilot.db.connection import get_connection
from pipeline_copilot.models import PipelineInvestigationRequest


class PipelineRunRepository:

    def find_runs_by_pipeline(
        self,
        request: PipelineInvestigationRequest,
    ) -> list[dict]:

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

            columns = [column[0] for column in cursor.description]

            return [
                dict(zip(columns, row))
                for row in cursor.fetchall()
            ]

        finally:
            connection.close()