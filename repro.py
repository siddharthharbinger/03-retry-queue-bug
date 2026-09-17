from datetime import datetime, timedelta

from retry import next_attempt


start = datetime(2026, 1, 1, 12, 0)
actual = [next_attempt(start, attempt).minute for attempt in (1, 2, 3)]
expected = [(start + timedelta(minutes=delay)).minute for delay in (1, 2, 4)]
print(f"actual={actual} expected={expected}")
raise SystemExit(0 if actual == expected else 1)
