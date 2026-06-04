# Local Run Metrics

This document describes the metrics currently computed by the ODL Observability tool based on local run summaries.

## Metrics Computed

- **Total Steps**: The total number of steps defined in the workflow execution.
- **Successful Steps**: The number of steps that finished with a `success` status.
- **Failed Steps**: The number of steps that finished with a `failed` status.
- **Artifact Count**: The total number of artifacts (files) produced during the run.
- **Workflow Status**: The overall status of the workflow execution (e.g., `success`, `failed`).
- **Duration**: The total time elapsed between the start and finish of the run, in seconds.

## Metric Meanings

- **Success Rate**: (Successful Steps / Total Steps) provides an indication of the workflow's reliability.
- **Execution Time**: The duration helps in identifying performance bottlenecks in the pipeline.
- **Artifact Yield**: The number of artifacts produced can be a sanity check for data ingestion and transformation steps.

## Limitations

- **Coarse-grained**: Metrics are based on the entire step execution, not sub-tasks within a step.
- **Local Context**: Metrics only reflect the local execution environment and do not account for external cloud service performance unless explicitly captured in the summary.
- **Manual Computation**: Metrics are computed after the run finishes, not in real-time.
