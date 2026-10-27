# 04: dependency loop

`clean` waits on `enrich` and `enrich` waits on `clean`, so neither can start. Validate passes, deploy fails with "circular dependencies are not allowed".

**The inspector says:** `task_dependency_loop` on both tasks.

**Fix:** remove one of the two `depends_on` entries.
