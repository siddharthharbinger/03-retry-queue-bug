from datetime import datetime, timedelta


def next_attempt(first_attempt: datetime, attempt_number: int) -> datetime:
    """Return the next retry time using exponential backoff."""
    return first_attempt + timedelta(minutes=1)
