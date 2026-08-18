import sqlite3

import pytest


@pytest.fixture
def test_connection():
    connection = sqlite3.connect(":memory:")

    connection.execute(
        """
        CREATE TABLE pipeline_run_log (
            run_id TEXT PRIMARY KEY,
            pipeline_name TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT,
            status TEXT NOT NULL,
            error_message TEXT,
            records_processed INTEGER
        )
        """
    )

    yield connection

    connection.close()