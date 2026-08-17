class PipelineCopilotError(Exception):
    """Base exception for the AI Data Pipeline Copilot."""


class ConfigurationError(PipelineCopilotError):
    """Raised when application configuration is invalid."""


class PipelineInvestigationError(PipelineCopilotError):
    """Raised when pipeline investigation fails."""