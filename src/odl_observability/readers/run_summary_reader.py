from __future__ import annotations
import json
from pathlib import Path
from ..models.run_summary import RunSummary

class RunSummaryReader:
    @staticmethod
    def read(path: str | Path) -> RunSummary:
        """Read a local run-summary.json and return a typed RunSummary model."""
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"Run summary file not found: {path}")
        
        try:
            with open(p, "r") as f:
                data = json.load(f)
            return RunSummary(**data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in run summary: {e}")
        except Exception as e:
            raise ValueError(f"Error reading run summary: {e}")
