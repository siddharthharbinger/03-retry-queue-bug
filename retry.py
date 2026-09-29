from datetime import datetime, timedelta


def next_attempt(first_attempt: datetime, attempt_number: int) -> datetime:
    """
    Return the next retry time using exponential backoff.

    The backoff interval doubles with each subsequent attempt:
        attempt_number = 1 → 1 minute
        attempt_number = 2 → 2 minutes
        attempt_number = 3 → 4 minutes
        ...
    """
    # Ensure attempt_number is at least 1 to avoid a zero or negative exponent.
    if attempt_number < 1:
        raise ValueError("attempt_number must be >= 1")

    backoff_minutes = 2 ** (attempt_number - 1)
    return first_attempt + timedelta(minutes=backoff_minutes)
