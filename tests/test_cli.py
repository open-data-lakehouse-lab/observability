import json
from typer.testing import CliRunner
from odl_observability.cli import app

runner = CliRunner()

def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "odl-observability version" in result.stdout

def test_cli_inspect_run(tmp_path):
    summary_data = {
        "run_id": "test-run",
        "workflow_name": "test-workflow",
        "dataset_id": "test-dataset",
        "resource": "test-resource",
        "status": "success",
        "started_at": "2026-06-04T22:15:00Z",
        "steps": [],
        "artifacts": []
    }
    summary_file = tmp_path / "run-summary.json"
    with open(summary_file, "w") as f:
        json.dump(summary_data, f)
        
    result = runner.invoke(app, ["inspect", "run", "--run-summary-path", str(summary_file)])
    assert result.exit_code == 0
    assert "test-run" in result.stdout

def test_cli_report_run(tmp_path):
    summary_data = {
        "run_id": "test-run",
        "workflow_name": "test-workflow",
        "dataset_id": "test-dataset",
        "resource": "test-resource",
        "status": "success",
        "started_at": "2026-06-04T22:15:00Z",
        "steps": [],
        "artifacts": []
    }
    summary_file = tmp_path / "run-summary.json"
    with open(summary_file, "w") as f:
        json.dump(summary_data, f)
        
    output_dir = tmp_path / "reports"
    result = runner.invoke(app, ["report", "run", "--run-summary-path", str(summary_file), "--output-dir", str(output_dir)])
    assert result.exit_code == 0
    assert (output_dir / "run-observability-report.json").exists()
    assert (output_dir / "run-observability-report.md").exists()

def test_cli_missing_file():
    result = runner.invoke(app, ["inspect", "run", "--run-summary-path", "non_existent.json"])
    assert result.exit_code != 0
    assert "Error" in result.stdout
