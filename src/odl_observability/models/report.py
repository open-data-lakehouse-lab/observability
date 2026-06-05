from __future__ import annotations
from typing import Optional
from pydantic import BaseModel
from .metrics import WorkflowMetrics

class FailedStepSummary(BaseModel):
    step_name: str
    command: str | list[str]
    return_code: int
    stderr: Optional[str] = None

    def command_as_text(self) -> str:
        if isinstance(self.command, list):
            return " ".join(self.command)
        return self.command

class ObservabilityReport(BaseModel):
    metrics: WorkflowMetrics
    health_status: str
    health_message: str
    failed_steps: list[FailedStepSummary] = []
