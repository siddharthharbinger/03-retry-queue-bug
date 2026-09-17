from datetime import datetime, timedelta

from retry import next_attempt


def test_retry_delay_uses_exponential_backoff():
    start = datetime(2026, 1, 1, 12, 0)
    assert next_attempt(start, 1) == start + timedelta(minutes=1)
    assert next_attempt(start, 2) == start + timedelta(minutes=2)
    assert next_attempt(start, 3) == start + timedelta(minutes=4)
