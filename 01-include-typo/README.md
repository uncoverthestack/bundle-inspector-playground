# 01: include typo

`databricks.yml` includes `resource/reports/*.yml`. The folder is `resources/reports/`. No file matches, and the CLI says nothing, so the `weekly_report` job is not part of the bundle. Deploy succeeds with one job instead of two.

**The inspector says:** `include_matches_nothing` on `databricks.yml`, with "Did you mean "resources/reports/*.yml"?", and `resource_not_included` on the job file.

**Fix:** add the missing "s".
