from pipeline_copilot.db.connection import get_connection


CREATE_PIPELINE_RUN_LOG_TABLE = """
CREATE TABLE IF NOT EXISTS pipeline_run_log (
    run_id TEXT PRIMARY KEY,
    pipeline_name TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT,
    status TEXT NOT NULL,
    error_message TEXT,
    records_processed INTEGER
);
"""


def create_tables() -> None:
    connection = get_connection()

    try:
        connection.execute(CREATE_PIPELINE_RUN_LOG_TABLE)
        connection.commit()
    finally:
        connection.close()