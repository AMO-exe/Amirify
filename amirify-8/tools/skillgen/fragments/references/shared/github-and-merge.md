# amirify reference: GitHub clone and cross-repo merge

Load this when the user passed one or more `https://github.com/...` URLs, or named several local subfolders to merge into one graph.

### Step 0 - Clone GitHub repo(s) (only if a GitHub URL was given)

**Single repo:**
```bash
LOCAL_PATH=$(amirify clone <github-url> [--branch <branch>])
# Use LOCAL_PATH as the target for all subsequent steps
```

**Multiple repos (cross-repo graph):**
```bash
# Clone each repo, run the full pipeline on each, then merge
amirify clone <url1>   # → ~/.amirify/repos/<owner1>/<repo1>
amirify clone <url2>   # → ~/.amirify/repos/<owner2>/<repo2>
# Run /amirify on each local path to produce their graph.json files
# Then merge:
amirify merge-graphs \
  ~/.amirify/repos/<owner1>/<repo1>/amirify-out/graph.json \
  ~/.amirify/repos/<owner2>/<repo2>/amirify-out/graph.json \
  --out amirify-out/cross-repo-graph.json
```

Amirify clones into `~/.amirify/repos/<owner>/<repo>` and reuses existing clones on repeat runs. Each node in the merged graph carries a `repo` attribute so you can filter by origin.

**Multiple local subfolders (monorepo or multi-service layout):**

The skill pipeline writes all intermediate and final outputs to `amirify-out/` in the current working directory. Running the skill on each subfolder separately will clobber the same output dir. Instead, use the CLI directly for each subfolder — it places `amirify-out/` *inside* the scanned path:

```bash
amirify extract ./core/     # → ./core/amirify-out/graph.json
amirify extract ./service/  # → ./service/amirify-out/graph.json
amirify extract ./platform/ # → ./platform/amirify-out/graph.json
# Add --backend gemini|kimi|openai|deepseek|claude-cli depending on which API key you have set

# Then merge at the project root:
amirify merge-graphs \
  ./core/amirify-out/graph.json \
  ./service/amirify-out/graph.json \
  ./platform/amirify-out/graph.json \
  --out amirify-out/graph.json
```

Once `amirify-out/graph.json` exists, the fast path above takes over: any codebase question runs `amirify query` directly on the merged graph — no re-extraction, no size gate.
