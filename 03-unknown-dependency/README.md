# 03: unknown dependency

The `report` task depends on `laod`. The job's task is `load`. Validate passes, deploy fails with "Invalid dependency graph".

**The inspector says:** `unknown_task_dependency`, with "Did you mean "load"?".

**Fix:** change `laod` to `load`.
