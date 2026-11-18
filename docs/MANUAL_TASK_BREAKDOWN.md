# Manual Task Breakdown Notes

Notes captured while performing the browser task manually with Playwright, to
guide how the agent should be prompted and how steps should be broken down.

## Task: Visit the QA Playground site and list all available products

### Observed manual steps
1. Navigate to the home URL: `https://qa-playground-automation-testing.onrender.com/`
2. Take a page snapshot (ARIA/accessibility tree) of the home page.
3. Analyze the snapshot to identify:
   - The "Products" navigation link (and its URL `/products`).
   - Featured products shown on the home page (optional, for completeness).
4. Navigate to the products page using the "Products" link.
5. Take a page snapshot of the products page.
6. Analyze the snapshot and collect all product names (headings) listed there.
7. Return the final list of product names as the result.

### Key takeaways for prompting the agent
- Always take a page snapshot after navigation before deciding the next action.
- Use the snapshot (not assumptions) to find links/targets and their URLs.
- When a step fails or the page differs from expectations, take a fresh snapshot
  and replan instead of repeating the same action.
- Only report what is actually visible on the page.
- The final output should be the result only, without steps or explanations.

## Observed issue: browser_snapshot returns empty after browser_navigate

### Background
While performing the manual task, the Playwright MCP tools were exercised
directly (without the agent) to understand their exact behavior and argument
requirements. This is necessary so the agent can be prompted correctly.

### What browser_navigate does
- Input: a `url` (string).
- Action: opens the URL in the browser.
- Output: a markdown-style result containing the Playwright code run, the page
  URL/title, and a reference to a saved snapshot file
  (e.g. `.playwright-mcp/page-*.yml`).

### What browser_snapshot does
- Inputs: `target`, `filename`, `depth`, `boxes` (all nullable in schema but
  the server rejects nulls in practice).
- Action: captures the accessibility (ARIA) tree of the current page.
- Output: a YAML-like snapshot of the page when valid arguments are supplied;
  an empty/invalid result when arguments are null or unsuitable.

### Observed manual behavior (step by step)
1. Call `browser_navigate(url=...)` only.
   - Result: navigation succeeds and a snapshot file reference is returned.
2. Call `browser_snapshot(target="", filename="", depth=10, boxes=False)` after
   navigation.
   - Result: full page snapshot is returned (headings, links, products, etc.).
3. Call `browser_snapshot()` with no arguments (all nulls).
   - Result: empty snapshot, because the server rejects null argument values.
4. Call `browser_snapshot` on a blank/unloaded page.
   - Result: empty snapshot.

### Impact on the agent
- The agent calls `browser_navigate` and then `browser_snapshot`, but often
  passes hallucinated or invalid arguments (nulls), so it receives an empty
  snapshot instead of the real page content.
- Because the snapshot is empty, the agent cannot find the needed links or
  products, so it repeats the same navigation + snapshot calls.
- This creates an infinite loop: repeated tool calls, growing token usage,
  until the token limit is exhausted or the user manually stops the run.

### Root cause
- The agent does not correctly reuse the snapshot already returned by
  `browser_navigate`.
- The agent does not know the correct argument shape for `browser_snapshot`
  (safe defaults: target="", filename="", depth=10, boxes=False).
- There is no guard enforcing valid snapshot arguments, so nulls reach the server.

### Notes for future prompting and implementation
- Prompt the agent to use the snapshot returned by `browser_navigate` first.
- If calling `browser_snapshot` again, instruct it to pass safe defaults
  (target="", filename="", depth=10, boxes=False) rather than nulls.
- Consider wrapping snapshot calls in a helper that always supplies valid
  arguments, removing the chance of nulls reaching the server.
- Add explicit verification steps so the agent checks for an empty snapshot
  and replans instead of repeating the same call.
