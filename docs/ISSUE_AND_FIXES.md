# Issues and Fixes

## Playwright MCP: Chromium distribution 'chrome' not found

### Issue
When running the Playwright MCP server, it failed with:
`Chromium distribution 'chrome' is not found at C:\Users\...\Google\Chrome\Application\chrome.exe`

### Cause
The Playwright MCP server tries to use the `chrome` browser installed on the machine
(under the path shown in the error), not a browser shipped with the MCP package itself.

### Fix
- Install Google Chrome on the desktop (standard installer). It gets installed at the
  path mentioned in the error (`C:\Users\<user>\AppData\Local\Google\Chrome\Application\chrome.exe`).
- Leave it as it is; then specifically mention the `chrome` browser in the Playwright
  MCP args so it launches the installed Google Chrome.

### Verification
- Google Chrome is installed at the expected path mentioned in the error.

## OpenRouter: NotFoundError (Stealth Crouton Alpha)

### Issue
`litellm.exceptions.NotFoundError: OpenrouterException - {"error":{"message":"Thank you for participating in the Stealth Crouton Alpha testing period...","code":404}}`

### Cause
The configured OpenRouter model (`openrouter/stealth/crouton-alpha`) was a free stealth/test model
that was retired after the testing period, so the provider returned 404.

### Fix
- Switched `OPENROUTER_MODEL` in `.env` to a different available OpenRouter free model
  (e.g. `openrouter/baidu/ernie-5.5-flash-preview:free`).

### Verification
- `.env` contains a currently available OpenRouter free model for `OPENROUTER_MODEL`.
