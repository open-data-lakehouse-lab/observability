from odl_observability.models.run_summary import RunSummary, RunStep
from odl_observability.metrics.workflow_metrics import WorkflowMetricsCalculator

def test_calculate_metrics_success():
    summary = RunSummary(
        run_id="run-1",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        started_at="2026-06-04T22:00:00Z",
        finished_at="2026-06-04T22:01:00Z",
        steps=[
            RunStep(step_name="s1", command="c1", return_code=0, status="success"),
            RunStep(step_name="s2", command="c2", return_code=0, status="success")
        ],
        artifacts=["a1", "a2", "a3"]
    )
    
    metrics = WorkflowMetricsCalculator.calculate(summary)
    
    assert metrics.total_steps == 2
    assert metrics.successful_steps == 2
    assert metrics.failed_steps == 0
    assert metrics.artifact_count == 3
    assert metrics.duration_seconds == 60.0

def test_calculate_metrics_failure():
    summary = RunSummary(
        run_id="run-2",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="failed",
        started_at="2026-06-04T22:00:00Z",
        finished_at="2026-06-04T22:00:30Z",
        steps=[
            RunStep(step_name="s1", command="c1", return_code=0, status="success"),
            RunStep(step_name="s2", command="c2", return_code=1, status="failed")
        ],
        artifacts=[]
    )
    
    metrics = WorkflowMetricsCalculator.calculate(summary)
    
    assert metrics.total_steps == 2
    assert metrics.successful_steps == 1
    assert metrics.failed_steps == 1
    assert metrics.duration_seconds == 30.0

def test_calculate_metrics_missing_duration():
    summary = RunSummary(
        run_id="run-3",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        started_at="2026-06-04T22:00:00Z",
        finished_at=None,
        steps=[],
        artifacts=[]
    )
    
    metrics = WorkflowMetricsCalculator.calculate(summary)
    assert metrics.duration_seconds is None
