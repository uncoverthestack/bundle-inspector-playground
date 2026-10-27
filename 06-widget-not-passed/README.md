# 06: widget not passed

`clean_orders.py` reads widget `schema`. The task passes `schema_name`. Validate and deploy pass, the run fails when the notebook reads the widget.

**The inspector says:** `widget_not_set` in the notebook, with "Did you mean "schema_name"?".

**Fix:** pass `schema` in `base_parameters`, or read `schema_name` in the notebook.
