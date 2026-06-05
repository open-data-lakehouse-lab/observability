from ..models.run_summary import RunSummary
from ..models.report import FailedStepSummary

class RunHealthValidator:
    @staticmethod
    def validate(run_summary: RunSummary) -> tuple[str, str, list[FailedStepSummary]]:
        """Validate run health and return status, message and failed steps."""
        failed_steps = [
            FailedStepSummary(
                step_name=step.step_name,
                command=step.command,
                return_code=step.return_code,
                stderr=step.stderr
            )
            for step in run_summary.steps if step.status.lower() == "failed"
        ]
        
        if not run_summary.steps:
            return "failure", "Run has no steps", failed_steps
            
        if run_summary.status.lower() not in ["success", "failed"]:
             return "failure", f"Unknown run status: {run_summary.status}", failed_steps

        if run_summary.status.lower() == "success" and failed_steps:
            return "failure", "Run status is success but failed steps exist", failed_steps
            
        if failed_steps:
            return "failure", f"Run has {len(failed_steps)} failed steps", failed_steps
            
        return "success", "Run is healthy", []
