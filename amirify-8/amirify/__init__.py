"""amirify - extract · build · cluster · analyze · report."""


def __getattr__(name):
    # Lazy imports so `amirify install` works before heavy deps are in place.
    _map = {
        "extract": ("amirify.extract", "extract"),
        "collect_files": ("amirify.extract", "collect_files"),
        "build_from_json": ("amirify.build", "build_from_json"),
        "cluster": ("amirify.cluster", "cluster"),
        "score_all": ("amirify.cluster", "score_all"),
        "cohesion_score": ("amirify.cluster", "cohesion_score"),
        "god_nodes": ("amirify.analyze", "god_nodes"),
        "surprising_connections": ("amirify.analyze", "surprising_connections"),
        "suggest_questions": ("amirify.analyze", "suggest_questions"),
        "generate": ("amirify.report", "generate"),
        "to_json": ("amirify.export", "to_json"),
        "to_html": ("amirify.export", "to_html"),
        "to_svg": ("amirify.export", "to_svg"),
        "to_canvas": ("amirify.export", "to_canvas"),
        "to_wiki": ("amirify.wiki", "to_wiki"),
        "reflect": ("amirify.reflect", "reflect"),
        "save_query_result": ("amirify.ingest", "save_query_result"),
    }
    if name in _map:
        import importlib
        mod_name, attr = _map[name]
        mod = importlib.import_module(mod_name)
        return getattr(mod, attr)
    raise AttributeError(f"module 'amirify' has no attribute {name!r}")
