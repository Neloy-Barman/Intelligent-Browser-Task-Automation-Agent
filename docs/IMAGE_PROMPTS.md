# Image Generation Prompts

This file collects image-generation prompts used for project documentation and
demo materials. Each section has a short header describing the intent of the
image, followed by the prompt.

## Architecture Diagram - Intelligent Browser Task Automation Agent

Intent: High-level system architecture overview for LinkedIn/demo, showing the
flow from user task input through the Streamlit frontend, CrewAI backend, LLM
provider, Playwright MCP server and browser, back to the user result, with
Arize Phoenix observability.

Prompt:
Generate a single clean, minimalist, professional architecture diagram image on a white background in flat 2D vector style with no 3D, crisp thin lines, rounded rectangles, consistent simple icons, readable sans-serif text, plenty of whitespace, and a 16:9 landscape layout, titled "Intelligent Browser Task Automation Agent — System Architecture" at the top center, showing a left-to-right flow where a User box with a person icon sends a "task input" arrow to a Frontend (Streamlit) box containing "Task Input" and "Result Output" sub-boxes, which sends an arrow to a Backend (CrewAI) box containing "Crew", "Browser Automation Agent", and "Task ({user_task})" sub-boxes, from which two arrows emerge: one labeled "LLM calls" pointing to an "LLM Provider (LM Studio / OpenRouter)" box tagged "temperature=0.6, timeout=120s", and one labeled "mcps" pointing to a "Playwright MCP Server (MCPServerStdio)" box tagged "crewai.mcp MCPServerStdio", which connects to a "Browser (Chrome/Chromium)" box labeled navigate, snapshot, click, type, wait, screenshot, which connects to a "Target Website" box with a globe icon, and a "final result" arrow returns from Backend (CrewAI) to Frontend (Streamlit) Result Output, with a full-width bottom band labeled "Observability & Evaluation" containing an "Arize Phoenix (Docker)" box with sub-labels "UI: localhost:6006" and "OTLP gRPC: localhost:4317" and dashed "traces" arrows pointing up to it from Backend (CrewAI), LLM Provider, and Playwright MCP Server, small pill badges "OpenInference instrumentation", "crewai.mcp MCPServerStdio", "OpenTelemetry", and "temperature=0.6, timeout=120s" placed near their relevant boxes, and a footer reading "Built with CrewAI + Playwright MCP + Phoenix", high resolution, no extra components beyond those named.
