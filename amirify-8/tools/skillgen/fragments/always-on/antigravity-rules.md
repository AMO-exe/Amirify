---
trigger: always_on
description: Consult the amirify knowledge graph at amirify-out/ for codebase and architecture questions.
---

## amirify

This project has an amirify knowledge graph at amirify-out/.

Rules:
- For codebase or architecture questions, when `amirify-out/graph.json` exists, first run `amirify query "<question>"` (CLI) or `query_graph` (MCP). Use `amirify path "<A>" "<B>"` / `shortest_path` for relationships and `amirify explain "<concept>"` / `get_node` for focused concepts. These return a scoped subgraph, usually much smaller than `GRAPH_REPORT.md` or raw grep output.
- If amirify-out/wiki/index.md exists, navigate it instead of reading raw files
- Read amirify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context
- After modifying code files in this session, run `amirify update .` to keep the graph current (AST-only, no API cost)
