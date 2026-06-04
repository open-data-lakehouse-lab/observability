# Observability Design

## Local-First Observability

The ODL Observability tool is designed with a local-first approach. It focuses on providing immediate feedback and visibility into the local data pipeline executions without the overhead of complex external systems.

## Run Summary Based Metrics

Metrics are derived directly from the `run-summary.json` files produced by the orchestration repository. This ensures that the observability is always in sync with the actual execution details.

## No External Observability Stack Yet

To maintain simplicity and zero-dependency during the initial phase, no external observability stacks (like Prometheus, Grafana, or OpenTelemetry) are introduced. This allows for a lightweight, CLI-based experience that works out-of-the-box in local environments.

## Future Integration with Orchestration

As the project evolves, the observability layer will be more tightly integrated with the orchestration repository, potentially allowing for real-time monitoring and more advanced lineage tracking.
