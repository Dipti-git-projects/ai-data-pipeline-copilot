from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field
from dataclasses import dataclass, field
from typing import Any

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

class FailurePattern(BaseModel):
    error_message: str
    occurrence_count: int
    run_ids: list[str]

class KnowledgeDocument(BaseModel):
    document_id: str
    title: str
    content: str
    source: str

# class DocumentChunk(BaseModel):
#     chunk_id: str
#     document_id: str
#     content: str
#     metadata: dict[str, str]

@dataclass
class DocumentChunk:

    chunk_id: str

    document_id: str

    content: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )