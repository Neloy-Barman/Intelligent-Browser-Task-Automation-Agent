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

## LM Studio: Request timed out (OpenAI API)

### Issue
`OpenAI API call failed: Failed to connect to OpenAI API: Request timed out.`

### Cause
LM Studio was restarted, which changed the backend IP address. The `.env` still pointed
`LM_STUDIO_BASE_URL` at the old IP (`http://169.254.11.190:1234/v1`), which was no longer
reachable, causing the connection timeout.

### Fix
- Updated `LM_STUDIO_BASE_URL` in `.env` to `http://localhost:1234/v1` (commenting out the
  stale IP-based URL), so it always resolves to the local LM Studio server regardless of
  IP changes.
- Added a 120s request timeout to the LLM in `config/llm_config.py`.

### Verification
- `http://localhost:1234/v1/models` responds successfully.
- LLM config loads with base URL `http://localhost:1234/v1`.

## Docker Desktop stuck at starting screen

### Issue
Docker Desktop was stuck on the starting screen.

### Cause / Steps
- Uninstalled the previous Docker and installed a newer version; then hit "virtualization is disabled in firmware".

### Fix
- Rebooted into BIOS (pressed the `Del` key repeatedly) -> Advanced mode -> Overclocking -> CPU Features -> enabled SVM (AMD virtualization).
- Saved & exited, rebooted; Docker Desktop started working.

### Verification
- Docker Desktop starts and runs normally.

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
