import json
import pytest
from odl_observability.readers.run_summary_reader import RunSummaryReader
from odl_observability.models.run_summary import RunSummary

def test_read_valid_run_summary(tmp_path):
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
    
    reader = RunSummaryReader()
    result = reader.read(summary_file)
    
    assert isinstance(result, RunSummary)
    assert result.run_id == "test-run"

def test_read_run_summary_with_list_command(tmp_path):
    summary_data = {
        "run_id": "test-run-list",
        "workflow_name": "test-workflow",
        "dataset_id": "test-dataset",
        "resource": "test-resource",
        "status": "success",
        "started_at": "2026-06-04T22:15:00Z",
        "steps": [
            {
                "step_name": "ingestion",
                "command": ["odl-ingestion", "ingest"],
                "return_code": 0,
                "status": "success"
            }
        ],
        "artifacts": []
    }
    summary_file = tmp_path / "run-summary-list.json"
    with open(summary_file, "w") as f:
        json.dump(summary_data, f)
    
    reader = RunSummaryReader()
    result = reader.read(summary_file)
    
    assert result.steps[0].command == ["odl-ingestion", "ingest"]
    assert result.steps[0].command_as_text() == "odl-ingestion ingest"

def test_read_missing_file():
    reader = RunSummaryReader()
    with pytest.raises(FileNotFoundError, match="Run summary file not found"):
        reader.read("non_existent_file.json")

def test_read_invalid_json(tmp_path):
    summary_file = tmp_path / "invalid.json"
    with open(summary_file, "w") as f:
        f.write("invalid json")
    
    reader = RunSummaryReader()
    with pytest.raises(ValueError, match="Invalid JSON in run summary"):
        reader.read(summary_file)
