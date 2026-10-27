# 05: duplicate task key

Two tasks are both called `load`. The CLI merges them into one task, later settings winning, so `load_orders.py` never runs. Nothing fails, which makes this one hard to spot.

**The inspector says:** `duplicate_task_key` on the second task, naming the line of the first.

**Fix:** give each task its own `task_key`.
