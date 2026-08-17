from pipeline_copilot.application import start_application
from pipeline_copilot.config import settings
from pipeline_copilot.logging_config import configure_logging


def main() -> None:
    configure_logging(settings.log_level)
    start_application()


if __name__ == "__main__":
    main()