# ODL Observability

Observability foundation for the Open Data Lakehouse Lab project.

## Purpose

The observability repository is responsible for local observability foundations, providing tools to monitor and analyze workflow executions from the orchestration repository.

## Scope

- Read local orchestration run summaries.
- Compute simple workflow execution metrics.
- Generate local observability reports (JSON and Markdown).
- Validate run health.
- Provide CLI-based observability workflows.
- Provide tests without network access or external services.

## Local-First Observability

This tool operates locally and does not require:
- Network access.
- API keys.
- External services (Prometheus, Grafana, etc.).

## Installation

```bash
# Install development dependencies
python3 -m pip install -r requirements-dev.txt

# Install the package in editable mode
python3 -m pip install -e .
```

## Usage

### CLI

The CLI is exposed as `odl-observability`.

#### Version
```bash
odl-observability version
```

#### Inspect a Run
```bash
odl-observability inspect run --run-summary-path ./examples/run-summary.json
```

#### Generate Reports
```bash
odl-observability report run \
  --run-summary-path ./examples/run-summary.json \
  --output-dir ./reports
```

### Validation

To run linting and tests:

```bash
bash scripts/validate.sh
```

## Metrics

The following metrics are currently computed:
- Total steps
- Successful steps
- Failed steps
- Artifact count
- Workflow status
- Duration in seconds

## License

Unless otherwise noted:

- Software, scripts, Infrastructure as Code, SQL models, configuration files and executable assets are licensed under the [Apache License 2.0](LICENSE).
- Documentation, diagrams and written content are licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Original upstream datasets, when referenced, remain governed by their original source licenses and terms.
