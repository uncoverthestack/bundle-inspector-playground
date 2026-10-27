# Bundle Inspector Playground

Small Databricks bundles that each pass `databricks bundle validate` but break when you deploy or run them. Open them with [Databricks Bundle Inspector](https://marketplace.visualstudio.com/items?itemName=UncoverTheStack.databricks-bundle-inspector) installed and watch the Problems panel catch each mistake, at the exact line, without clicking anything.

No Databricks account is needed. The inspector checks the bundle inside your editor, without signing in.

## Try it in your browser

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/uncoverthestack/bundle-inspector-playground)

This opens VS Code in your browser with the Databricks CLI and the inspector already installed. When it has loaded, open the Problems panel (`Ctrl+Shift+M`). It needs a GitHub account and uses a little of your free Codespaces time.

## Try it on your machine

1. Install the [Databricks CLI](https://docs.databricks.com/dev-tools/cli/install.html) and the [Bundle Inspector](https://marketplace.visualstudio.com/items?itemName=UncoverTheStack.databricks-bundle-inspector) extension. In Cursor or Windsurf, get it from [Open VSX](https://open-vsx.org/extension/UncoverTheStack/databricks-bundle-inspector).
2. Clone this repo and open the whole folder in VS Code.
3. Open the Problems panel (`Ctrl+Shift+M`, or `Cmd+Shift+M` on a Mac).

Each folder is its own bundle. Fix a mistake, save, and its warning goes away.

## What's in each folder

| Folder | The mistake | `bundle validate` | What actually happens |
|---|---|---|---|
| [01-include-typo](01-include-typo) | `include` says `resource/` instead of `resources/` | OK | A whole job is silently left out of the deploy |
| [02-gitignored-file](02-gitignored-file) | A task runs a file that `.gitignore` skips | OK | The file is never uploaded, so the run can't find it |
| [03-unknown-dependency](03-unknown-dependency) | `depends_on` names `laod` instead of `load` | OK | Deploy fails: "Invalid dependency graph" |
| [04-dependency-loop](04-dependency-loop) | Two tasks wait on each other | OK | Deploy fails: "circular dependencies are not allowed" |
| [05-duplicate-task-key](05-duplicate-task-key) | Two tasks share one `task_key` | OK | They are merged into one task, so one notebook never runs |
| [06-widget-not-passed](06-widget-not-passed) | The notebook reads widget `schema`, the task passes `schema_name` | OK | The run fails when the notebook reads the widget |
| [07-task-value-not-set](07-task-value-not-set) | A task reads task value `rowcount`, the upstream task sets `row_count` | OK | The run fails on the missing key |
| [08-pipeline-missing-source](08-pipeline-missing-source) | A pipeline's glob points at `transformation/`, the folder is `transformations/` | OK | The pipeline has no source files |
| [09-secret-scope-key](09-secret-scope-key) | Code reads secret scope `api_keys`, the bundle's key, not its name | OK | The run fails: no scope called `api_keys` |
| [clean](clean) | Nothing. A correct bundle | OK | Runs. Break it yourself with [BREAK_IT.md](BREAK_IT.md) |

## Break it yourself

[BREAK_IT.md](BREAK_IT.md) lists edits to make in `clean/` and what the inspector should say for each.

## It missed something?

If you broke a bundle and the inspector said nothing, or it warned about something that works, [open an issue](../../issues/new?template=missed-catch.yml). Say what you changed and which Databricks CLI version you have (`databricks --version`). Those reports are the most useful feedback the project gets.

## How these were checked

Every folder, and every edit in [BREAK_IT.md](BREAK_IT.md), was run through `databricks bundle validate -t dev` (CLI v1.21.0) and through the inspector's own checks. The `bundle validate` and inspector results above come from those runs.

The "What actually happens" column: 03 to 07 were seen on a real workspace. 01 was seen in the CLI's output, which lists one job, not two. 02, 08 and 09 follow how the CLI and Databricks are documented to behave, and have not been run on a workspace yet.

## Telemetry

The extension asks before it sends anonymous usage data. See [what it collects](https://github.com/uncoverthestack/databricks-bundle-inspector/blob/main/docs/telemetry.md).
