# 02: gitignored file

The `backfill` task runs `scratch/backfill.py`. `.gitignore` lists `scratch/`, and `bundle deploy` skips gitignored files, so the file is never uploaded and the run can't find it.

**The inspector says:** `excluded_from_sync` on the task's `python_file` line.

**Fix:** remove `scratch/` from `.gitignore`, or add the file to `sync.include` in `databricks.yml`.
