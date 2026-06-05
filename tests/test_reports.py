import json
from odl_observability.models.metrics import WorkflowMetrics
from odl_observability.models.report import ObservabilityReport
from odl_observability.reports.json_report import JsonReportWriter
from odl_observability.reports.markdown_report import MarkdownReportWriter

def test_json_report_writer(tmp_path):
    metrics = WorkflowMetrics(
        run_id="run-1",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        total_steps=1,
        successful_steps=1,
        failed_steps=0,
        artifact_count=0
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="success",
        health_message="OK"
    )
    
    output_dir = tmp_path / "reports"
    report_path = JsonReportWriter.write(report, output_dir)
    
    assert report_path.exists()
    with open(report_path, "r") as f:
        data = json.load(f)
    assert data["metrics"]["run_id"] == "run-1"

def test_markdown_report_writer(tmp_path):
    metrics = WorkflowMetrics(
        run_id="run-1",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        total_steps=1,
        successful_steps=1,
        failed_steps=0,
        artifact_count=0
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="success",
        health_message="OK"
    )
    
    output_dir = tmp_path / "reports"
    report_path = MarkdownReportWriter.write(report, output_dir)
    
    assert report_path.exists()
    content = report_path.read_text()
    assert "# Observability Report - run-1" in content
    assert "## Summary" in content
    assert "## Metrics" in content

def test_markdown_report_failed_steps(tmp_path):
    from odl_observability.models.report import FailedStepSummary
    metrics = WorkflowMetrics(
        run_id="run-fail",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="failed",
        total_steps=1,
        successful_steps=0,
        failed_steps=1,
        artifact_count=0
    )
    report = ObservabilityReport(
        metrics=metrics,
        health_status="failure",
        health_message="Run has failed steps",
        failed_steps=[
            FailedStepSummary(
                step_name="s1",
                command=["cmd", "--error"],
                return_code=1,
                stderr="some error"
            )
        ]
    )
    
    output_dir = tmp_path / "reports-fail"
    report_path = MarkdownReportWriter.write(report, output_dir)
    
    content = report_path.read_text()
    assert "## Failed Steps" in content
    assert "### s1" in content
    assert "**Command**: `cmd --error`" in content
    assert "**Return Code**: 1" in content
    assert "some error" in content
