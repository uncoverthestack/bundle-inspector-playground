# 09: secret scope key instead of name

The bundle defines a secret scope under the key `api_keys`, with the name `playground-api-keys`. The notebook reads scope `api_keys`. In Databricks the scope is called by its name, so the read fails unless another scope called `api_keys` exists.

**The inspector says:** `secret_scope_name_mismatch`, with "Did you mean "playground-api-keys"?".

**Fix:** use `scope="playground-api-keys"`.
