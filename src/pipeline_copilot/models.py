from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class PipelineStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    RUNNING = "RUNNING"


class PipelineInvestigationRequest(BaseModel):
    pipeline_name: str = Field(min_length=1)
    run_id: str | None = None


class PipelineRun(BaseModel):
    run_id: str
    pipeline_name: str
    start_time: datetime
    end_time: datetime | None = None
    status: PipelineStatus
    error_message: str | None = None
    records_processed: int | None = None