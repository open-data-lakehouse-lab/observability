from ..models.run_summary import RunSummary
from ..models.metrics import WorkflowMetrics
from ..utils.dates import calculate_duration_seconds

class WorkflowMetricsCalculator:
    @staticmethod
    def calculate(run_summary: RunSummary) -> WorkflowMetrics:
        """Compute metrics from a RunSummary."""
        total_steps = len(run_summary.steps)
        successful_steps = sum(1 for step in run_summary.steps if step.status.lower() == "success")
        failed_steps = sum(1 for step in run_summary.steps if step.status.lower() == "failed")
        
        duration = calculate_duration_seconds(run_summary.started_at, run_summary.finished_at)
        
        return WorkflowMetrics(
            run_id=run_summary.run_id,
            workflow_name=run_summary.workflow_name,
            dataset_id=run_summary.dataset_id,
            resource=run_summary.resource,
            status=run_summary.status,
            total_steps=total_steps,
            successful_steps=successful_steps,
            failed_steps=failed_steps,
            artifact_count=len(run_summary.artifacts),
            duration_seconds=duration
        )
