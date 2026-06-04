from datetime import datetime
from typing import Optional

def parse_iso_datetime(dt_str: str) -> datetime:
    """Parse ISO 8601 datetime string."""
    return datetime.fromisoformat(dt_str.replace("Z", "+00:00"))

def calculate_duration_seconds(start_time: str, end_time: Optional[str]) -> Optional[float]:
    """Calculate duration between two ISO 8601 strings in seconds."""
    if not end_time:
        return None
    try:
        start = parse_iso_datetime(start_time)
        end = parse_iso_datetime(end_time)
        return (end - start).total_seconds()
    except (ValueError, TypeError):
        return None
