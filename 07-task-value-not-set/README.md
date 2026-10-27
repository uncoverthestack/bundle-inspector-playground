# 07: task value not set

`publish.py` reads task value `rowcount` from `ingest`. `ingest.py` sets `row_count`. Validate and deploy pass, the run fails on the missing key.

**The inspector says:** `task_value_key_not_set` in `publish.py`, with "Did you mean "row_count"?".

**Fix:** use the same key in both files.
