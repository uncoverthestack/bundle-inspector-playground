# 08: pipeline glob with no files

The pipeline's sources are `transformation/**`. The SQL files are in `transformations/`. Validate passes, and the pipeline gets no source files.

A misspelled single `file:` path is caught by `bundle validate` in CLI v1.21.0. A glob that matches nothing is not.

**The inspector says:** `missing_pipeline_source` on the glob.

**Fix:** change the glob to `../transformations/**`.
