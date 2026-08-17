from pipeline_copilot.db.connection import get_connection


SAMPLE_RUNS = [
    (
        "RUN1001",
        "CUSTOMER_INCREMENTAL_LOAD",
        "2026-08-14 08:00:00",
        "2026-08-14 08:15:00",
        "SUCCESS",
        None,
        125000,
    ),
    (
        "RUN1002",
        "CUSTOMER_INCREMENTAL_LOAD",
        "2026-08-15 08:00:00",
        "2026-08-15 08:03:00",
        "FAILED",
        "Snowflake connection timeout",
        0,
    ),
    (
        "RUN1003",
        "CUSTOMER_INCREMENTAL_LOAD",
        "2026-08-16 08:00:00",
        "2026-08-16 08:02:00",
        "FAILED",
        "Snowflake connection timeout",
        0,
    ),
    (
        "RUN1004",
        "CUSTOMER_INCREMENTAL_LOAD",
        "2026-08-17 08:00:00",
        "2026-08-17 08:20:00",
        "SUCCESS",
        None,
        130000,
    ),
]


def seed_database() -> None:

    connection = get_connection()

    try:
        connection.executemany(
            """
            INSERT OR REPLACE INTO pipeline_run_log (
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
            SAMPLE_RUNS,
        )

        connection.commit()

    finally:
        connection.close()


if __name__ == "__main__":
    from pipeline_copilot.db.schema import create_tables

    create_tables()
    seed_database()

    print("Sample pipeline logs inserted.")