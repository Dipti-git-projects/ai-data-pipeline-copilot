import logging

from pipeline_copilot.config import settings


logger = logging.getLogger(__name__)


def start_application() -> None:
    logger.info(
        "Starting %s in %s environment",
        settings.app_name,
        settings.environment,
    )