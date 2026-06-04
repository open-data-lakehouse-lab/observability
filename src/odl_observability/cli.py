import typer
from pathlib import Path

from .readers.run_summary_reader import RunSummaryReader
from .metrics.workflow_metrics import WorkflowMetricsCalculator
from .validation.run_health import RunHealthValidator
from .models.report import ObservabilityReport
from .reports.json_report import JsonReportWriter
from .reports.markdown_report import MarkdownReportWriter

app = typer.Typer(help="ODL Observability CLI")
inspect_app = typer.Typer(help="Inspect run summaries")
report_app = typer.Typer(help="Generate observability reports")

app.add_typer(inspect_app, name="inspect")
app.add_typer(report_app, name="report")

@app.command()
def version() -> None:
    """Print the version of the ODL Observability CLI."""
    typer.echo("odl-observability version 0.1.0")

@inspect_app.command("run")
def inspect_run(
    run_summary_path: Path = typer.Option(..., help="Path to the run summary JSON file")
) -> None:
    """Inspect a run summary and print a human-readable summary."""
    try:
        run_summary = RunSummaryReader.read(run_summary_path)
        metrics = WorkflowMetricsCalculator.calculate(run_summary)
        health_status, health_message, _ = RunHealthValidator.validate(run_summary)
        
        typer.secho(f"Run Summary Inspection: {run_summary.run_id}", fg=typer.colors.CYAN, bold=True)
        typer.echo(f"Workflow: {run_summary.workflow_name}")
        typer.echo(f"Dataset: {run_summary.dataset_id}")
        typer.echo(f"Status: {run_summary.status}")
        typer.echo(f"Health: {health_status} ({health_message})")
        typer.echo("-" * 20)
        typer.echo(f"Total steps: {metrics.total_steps}")
        typer.echo(f"Successful steps: {metrics.successful_steps}")
        typer.echo(f"Failed steps: {metrics.failed_steps}")
        typer.echo(f"Artifacts: {metrics.artifact_count}")
        if metrics.duration_seconds:
            typer.echo(f"Duration: {metrics.duration_seconds:.2f}s")
            
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

@report_app.command("run")
def report_run(
    run_summary_path: Path = typer.Option(..., help="Path to the run summary JSON file"),
    output_dir: Path = typer.Option(Path("./reports"), help="Directory to write reports")
) -> None:
    """Generate observability reports (JSON and Markdown)."""
    try:
        run_summary = RunSummaryReader.read(run_summary_path)
        metrics = WorkflowMetricsCalculator.calculate(run_summary)
        health_status, health_message, failed_steps = RunHealthValidator.validate(run_summary)
        
        report = ObservabilityReport(
            metrics=metrics,
            health_status=health_status,
            health_message=health_message,
            failed_steps=failed_steps
        )
        
        json_path = JsonReportWriter.write(report, output_dir)
        md_path = MarkdownReportWriter.write(report, output_dir)
        
        typer.secho(f"Reports generated successfully in {output_dir}", fg=typer.colors.GREEN)
        typer.echo(f"- JSON report: {json_path}")
        typer.echo(f"- Markdown report: {md_path}")
        
    except Exception as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
