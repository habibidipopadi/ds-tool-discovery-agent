# DS Tool Discovery Agent

AI agent that periodically discovers, evaluates, and ranks powerful data science tools from sources like GitHub, PyPI, and Hugging Face.

## High-level architecture

- Discovery workers for each source (GitHub, PyPI, Hugging Face)
- Evaluation & scoring using heuristics + LLM
- PostgreSQL (or Supabase) as canonical registry
- MCP server exposing a `search_tools` and `get_tool_details` interface
- Optional n8n workflows for scheduling runs and sending alerts
