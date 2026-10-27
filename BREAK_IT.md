# Break it yourself

Open `clean/` and make one of these edits. Save the file and watch the Problems panel. Undo the edit (`Ctrl+Z`, then save) before the next one.

The first eight pass `databricks bundle validate`, so the inspector is the only warning you get before deploy. The last three are also caught by validate. They're here to show the inspector flags them while you type, with a fix in the light bulb.

| Edit | File | What the inspector says |
|---|---|---|
| In `clean`'s `depends_on`, change `ingest` to `ingst` | `resources/orders.job.yml` | `unknown_task_dependency`, "Did you mean "ingest"?". Also `task_value_not_upstream` in `publish.py`, since `ingest` no longer runs before it |
| Give `ingest` a `depends_on` on `publish` | `resources/orders.job.yml` | `task_dependency_loop` on all three tasks |
| Rename the `clean` task's `task_key` to `publish` | `resources/orders.job.yml` | `duplicate_task_key`, and `unknown_task_dependency` because `publish` still waits on `clean` |
| Change `schema: sales` to `schemas: sales` | `resources/orders.job.yml` | `widget_not_set` in `src/clean.py`, "Did you mean "schemas"?" |
| Change `key="row_count"` to `key="rows"` | `src/ingest.py` | `task_value_key_not_set` in `src/publish.py` |
| Delete `publish`'s `depends_on` | `resources/orders.job.yml` | `task_value_not_upstream` in `src/publish.py` |
| Add a line `src/` | `.gitignore` | `excluded_from_sync` on every task |
| Change `resources/*.yml` to `resources/*.yaml` | `databricks.yml` | `include_matches_nothing`, "Did you mean "resources/*.yml"?" |
| Change `../src/clean.py` to `../src/clen.py` | `resources/orders.job.yml` | `missing_file`, with a Quick Fix. Validate catches it too |
| Change `../src/clean.py` to `../src/clean` | `resources/orders.job.yml` | `notebook_missing_extension`, with a Quick Fix. Validate catches it too |
| Delete the first line, `# Databricks notebook source` | `src/clean.py` | `not_a_notebook`. Validate catches it too |

Every finding's code in the Problems panel links to its explanation in the [list of checks](https://github.com/uncoverthestack/databricks-bundle-inspector/blob/main/docs/checks.md).
