from typing import Optional
from pydantic import BaseModel

class WorkflowMetrics(BaseModel):
    run_id: str
    workflow_name: str
    dataset_id: str
    resource: str
    status: str
    total_steps: int
    successful_steps: int
    failed_steps: int
    artifact_count: int
    duration_seconds: Optional[float] = None
