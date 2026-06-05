from odl_observability.models.run_summary import RunSummary, RunStep
from odl_observability.validation.run_health import RunHealthValidator

def test_health_success():
    summary = RunSummary(
        run_id="run-1",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        started_at="2026-06-04T22:00:00Z",
        steps=[
            RunStep(step_name="s1", command="c1", return_code=0, status="success")
        ]
    )
    status, msg, failed = RunHealthValidator.validate(summary)
    assert status == "success"
    assert not failed

def test_health_failed_step():
    summary = RunSummary(
        run_id="run-2",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="failed",
        started_at="2026-06-04T22:00:00Z",
        steps=[
            RunStep(step_name="s1", command="c1", return_code=1, status="failed")
        ]
    )
    status, msg, failed = RunHealthValidator.validate(summary)
    assert status == "failure"
    assert len(failed) == 1
    assert failed[0].command == "c1"

def test_health_failed_step_list_command():
    summary = RunSummary(
        run_id="run-list",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="failed",
        started_at="2026-06-04T22:00:00Z",
        steps=[
            RunStep(step_name="s1", command=["c1", "--arg"], return_code=1, status="failed")
        ]
    )
    status, msg, failed = RunHealthValidator.validate(summary)
    assert status == "failure"
    assert len(failed) == 1
    assert failed[0].command == ["c1", "--arg"]
    assert failed[0].command_as_text() == "c1 --arg"

def test_health_no_steps():
    summary = RunSummary(
        run_id="run-3",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        started_at="2026-06-04T22:00:00Z",
        steps=[]
    )
    status, msg, failed = RunHealthValidator.validate(summary)
    assert status == "failure"
    assert "no steps" in msg.lower()

def test_health_mismatch_status():
    summary = RunSummary(
        run_id="run-4",
        workflow_name="wf",
        dataset_id="ds",
        resource="res",
        status="success",
        started_at="2026-06-04T22:00:00Z",
        steps=[
            RunStep(step_name="s1", command="c1", return_code=1, status="failed")
        ]
    )
    status, msg, failed = RunHealthValidator.validate(summary)
    assert status == "failure"
    assert "mismatch" in msg.lower() or "success but failed steps exist" in msg.lower()
