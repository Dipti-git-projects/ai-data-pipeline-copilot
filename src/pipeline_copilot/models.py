from pydantic import BaseModel, Field


class PipelineInvestigationRequest(BaseModel):
    pipeline_name: str = Field(min_length=1)
    run_id: str | None = None