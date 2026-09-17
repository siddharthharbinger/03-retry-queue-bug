# Retry Queue Bug

High-level bug: `next_attempt` schedules every retry at the original time instead of applying exponential backoff. This causes repeated failures to hammer the dependency and violates the retry contract.

Run the reproduction with:

```powershell
python repro.py
```

Run the failing test with:

```powershell
python -m pytest -q
```

Expected retry delays are 1, 2, and 4 minutes for attempts 1, 2, and 3.
