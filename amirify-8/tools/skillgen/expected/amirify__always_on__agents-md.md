## amirify

This project has a knowledge graph at amirify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/amirify`, use the installed amirify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `amirify query "<question>"` when amirify-out/graph.json exists. Use `amirify path "<A>" "<B>"` for relationships and `amirify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty amirify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip amirify. Only skip amirify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If amirify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read amirify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `amirify update .` to keep the graph current (AST-only, no API cost).
