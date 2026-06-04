from typing import Optional
from pydantic import BaseModel, Field

class RunStep(BaseModel):
    step_name: str
    command: str
    return_code: int
    stdout: Optional[str] = None
    stderr: Optional[str] = None
    status: str

class RunSummary(BaseModel):
    run_id: str
    workflow_name: str
    dataset_id: str
    resource: str
    status: str
    started_at: str
    finished_at: Optional[str] = None
    steps: list[RunStep] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
