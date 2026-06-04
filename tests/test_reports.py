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
