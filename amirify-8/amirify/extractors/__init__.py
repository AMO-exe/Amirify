"""Per-language extractors, incrementally migrated out of amirify/extract.py.

Dispatch still flows through amirify.extract (the facade re-exports every
moved name), so importing from amirify.extract keeps working unchanged.
LANGUAGE_EXTRACTORS is the registry seed; wiring dispatch through it is a
later, separate step. See MIGRATION.md for how to port another language.
"""
from __future__ import annotations

from pathlib import Path
from typing import Callable

from amirify.extractors.apex import extract_apex
from amirify.extractors.bash import extract_bash
from amirify.extractors.blade import extract_blade
from amirify.extractors.cobol import extract_cobol
from amirify.extractors.commonlisp import extract_commonlisp
from amirify.extractors.dart import extract_dart
from amirify.extractors.dm import extract_dm, extract_dmf, extract_dmi, extract_dmm
from amirify.extractors.elixir import extract_elixir
from amirify.extractors.erlang import extract_erlang
from amirify.extractors.fortran import extract_fortran
from amirify.extractors.go import extract_go
from amirify.extractors.json_config import extract_json
from amirify.extractors.julia import extract_julia
from amirify.extractors.markdown import extract_markdown
from amirify.extractors.objc import extract_objc
from amirify.extractors.pascal import extract_pascal
from amirify.extractors.pascal_forms import extract_delphi_form, extract_lazarus_form
from amirify.extractors.powershell import extract_powershell, extract_powershell_manifest
from amirify.extractors.r import extract_r
from amirify.extractors.razor import extract_razor
from amirify.extractors.rust import extract_rust
from amirify.extractors.sln import extract_sln
from amirify.extractors.solidity import extract_solidity
from amirify.extractors.sql import extract_sql
from amirify.extractors.terraform import extract_terraform
from amirify.extractors.verilog import extract_verilog
from amirify.extractors.vbnet import extract_vbnet
from amirify.extractors.zig import extract_zig

LANGUAGE_EXTRACTORS: dict[str, Callable[[Path], dict]] = {
    "apex": extract_apex,
    "bash": extract_bash,
    "blade": extract_blade,
    "cobol": extract_cobol,
    "commonlisp": extract_commonlisp,
    "dart": extract_dart,
    "delphi_form": extract_delphi_form,
    "dm": extract_dm,
    "dmf": extract_dmf,
    "dmi": extract_dmi,
    "dmm": extract_dmm,
    "elixir": extract_elixir,
    "erlang": extract_erlang,
    "fortran": extract_fortran,
    "go": extract_go,
    "json": extract_json,
    "julia": extract_julia,
    "lazarus_form": extract_lazarus_form,
    "markdown": extract_markdown,
    "objc": extract_objc,
    "pascal": extract_pascal,
    "powershell": extract_powershell,
    "powershell_manifest": extract_powershell_manifest,
    "r": extract_r,
    "razor": extract_razor,
    "rust": extract_rust,
    "sln": extract_sln,
    "solidity": extract_solidity,
    "sql": extract_sql,
    "terraform": extract_terraform,
    "verilog": extract_verilog,
    "vbnet": extract_vbnet,
    "zig": extract_zig,
}
