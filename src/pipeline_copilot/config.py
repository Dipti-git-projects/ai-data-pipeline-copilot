import os


def get_environment() -> str:
    return os.getenv("APP_ENV", "development")