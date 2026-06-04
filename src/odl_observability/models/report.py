from typing import Optional
from pydantic import BaseModel
from .metrics import WorkflowMetrics

class FailedStepSummary(BaseModel):
    step_name: str
    return_code: int
    stderr: Optional[str] = None

class ObservabilityReport(BaseModel):
    metrics: WorkflowMetrics
    health_status: str
    health_message: str
    failed_steps: list[FailedStepSummary] = []
