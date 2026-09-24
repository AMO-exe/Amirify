## amirify

This project has a knowledge graph at amirify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `amirify query "<question>"` when amirify-out/graph.json exists. Use `amirify path "<A>" "<B>"` for relationships and `amirify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If amirify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read amirify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `amirify update .` to keep the graph current (AST-only, no API cost).
