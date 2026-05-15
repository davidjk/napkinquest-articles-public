"""
Smoke test for build.py + prose<->spreadsheet consistency for index.md.

Regenerates the workbook end-to-end into a temp file, evaluates every formula
with the `formulas` package, and asserts two things:

1. Cell regression: key cell values match the issue-body reference numbers
   and the existing model's totals.
2. Prose<->model linkage: for checks with `prose_patterns`, at least one of
   the patterns must match somewhere in index.md. Any-of semantics: the first
   pattern that matches counts as a pass. Catches drift where the model is
   updated but the article still quotes the old figure (or vice versa).

External facts (training costs, deal sizes, GW commitments) are out of scope:
the register only covers numbers the model produces.

Run with:
    python3 verify.py
(cwd-independent: resolves build.py and index.md next to itself.)

Exits 0 on PASS, 1 on FAIL.
"""

import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

import formulas
import numpy as np


HERE = Path(__file__).resolve().parent
BUILD_SCRIPT = HERE / "build.py"
INDEX_MD = HERE / "index.md"


def evaluate(xlsx_path):
    sol = formulas.ExcelModel().loads(str(xlsx_path)).finish().calculate()
    name = Path(xlsx_path).name

    def get(sheet, cell):
        key = f"'[{name}]{sheet.upper()}'!{cell}"
        if key not in sol:
            return None
        v = sol[key].value
        if isinstance(v, np.ndarray):
            v = v.flat[0]
        return v

    return get


@dataclass
class Check:
    label: str
    sheet: str
    cell: str
    expected: float
    tolerance: float
    # If non-empty, at least one pattern must match somewhere in index.md.
    # Patterns are regex strings, OR-combined (any match passes).
    prose_patterns: list[str] = field(default_factory=list)
    # Free-text hint for failure messages (e.g., "lede / five-layer summary").
    section_hint: str = ""


# Register. Each entry locks (sheet, cell, expected, tolerance). Entries with
# `prose_patterns` additionally pin the figure to a phrasing in index.md.
#
# Pattern conventions:
#   - Use word boundaries (\b) on dollar figures so "$154" doesn't match "$1540".
#   - Use the rounded form readers will see (e.g. $154, not 154.25).
#   - Provide multiple alternatives if the article might phrase the figure
#     several ways ("$154/M" vs "$154 per million").
CHECKS = [
    # --- Cost Build totals (these anchor the "lab cash vs full economic" basis) ---
    Check(
        "Cost Build lab cash $/M (Mid)", "Cost Build", "D38", 154.25, 0.5,
        prose_patterns=[r"\$154\b"],
        section_hint="five-layer summary / basis-as-thesis-device",
    ),
    Check(
        "Cost Build full economic $/M (Mid)", "Cost Build", "D39", 252.92, 0.5,
        prose_patterns=[r"\$253\b"],
        section_hint="five-layer summary / basis-as-thesis-device",
    ),
    # --- Breakeven block (full-economic price + demand-implied math) ---
    Check(
        "Breakeven full-econ price (Mid)", "Breakeven", "D6", 252.92, 0.5,
        # mirrors Cost Build D39 — no separate prose pattern needed
    ),
    Check(
        "Breakeven price multiple over yield (Mid)", "Breakeven", "D9", 1.9, 0.1,
    ),
    Check(
        "Breakeven tokens needed at today's revenue (Mid, T)", "Breakeven", "D14", 25.5, 1.0,
        prose_patterns=[r"25\s*trillion", r"25\.5\s*trillion", r"\b25T\b"],
        section_hint="demand-implied section / breakeven floor",
    ),
    # --- No-Subsidy Pricing block ---
    Check(
        "No-Subsidy median Mid monthly cost ($38)", "No-Subsidy Pricing", "D18", 37.94, 1.0,
    ),
    Check(
        "No-Subsidy power Mid monthly cost ($506)", "No-Subsidy Pricing", "D27", 505.85, 2.0,
    ),
    # --- Implicit Demand block (the thesis-driving numbers) ---
    Check(
        "Implicit Demand Anthropic Mid (~158T/yr)", "Implicit Demand", "D9", 158.1, 1.0,
        prose_patterns=[r"158\s*trillion", r"158\s*T\b"],
        section_hint="demand-implied section",
    ),
    Check(
        "Implicit Demand OpenAI Mid (~237T/yr)", "Implicit Demand", "D15", 237.2, 2.0,
        prose_patterns=[r"237\s*trillion", r"237\s*T\b"],
        section_hint="demand-implied section",
    ),
    Check(
        "Implicit Demand industry total (~474T/yr)", "Implicit Demand", "D26", 474.4, 3.0,
        prose_patterns=[r"474\s*trillion", r"474\s*T\b"],
        section_hint="demand-implied section",
    ),
    Check(
        "Implicit Demand growth multiple Mid (~1.9x)", "Implicit Demand", "D29", 1.9, 0.1,
        prose_patterns=[r"\b1\.9x\b", r"1\.9-?times"],
        section_hint="demand-implied section",
    ),
    # --- Plausibility lenses ---
    Check(
        "Plausibility heavy-user equiv (Mid, ~19.8M)", "Plausibility", "D8", 19.77, 0.5,
        prose_patterns=[r"19\.8\s*million", r"19\.8M\b"],
        section_hint="demand-implied plausibility check",
    ),
    Check(
        "Plausibility seats needed (Mid, 40M)", "Plausibility", "D13", 40.0, 1.0,
        prose_patterns=[r"40\s*million\s+(?:paying\s+)?seats", r"40M\s+seats"],
        section_hint="demand-implied plausibility check",
    ),
    Check(
        "Plausibility growth multiple (Mid, ~1.9x)", "Plausibility", "D16", 1.9, 0.1,
        # mirrors Implicit Demand D29 — same number, same prose match
    ),
    # --- Capex Perspective ---
    Check(
        "Capex Perspective per-lab bps of GDP (Mid)", "Capex Perspective", "D10", 24.83, 0.5,
    ),
    Check(
        "Capex Perspective annual rate % GDP (Mid)", "Capex Perspective", "D20", 0.00414, 0.0005,
    ),
    Check(
        "Capex Perspective implied hardware capex (Mid, $72B)", "Capex Perspective", "D25", 72.0, 1.0,
    ),
    Check(
        "Capex Perspective new DC MW added (Mid)", "Capex Perspective", "D26", 1800, 50,
    ),
]


def main():
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as f:
        out = f.name

    result = subprocess.run(
        [sys.executable, str(BUILD_SCRIPT), out],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print("FAIL: build script crashed")
        print(result.stderr)
        sys.exit(1)

    get = evaluate(out)
    prose = INDEX_MD.read_text() if INDEX_MD.exists() else ""

    cell_failures = []
    prose_failures = []
    prose_checked = 0

    for check in CHECKS:
        v = get(check.sheet, check.cell)
        if v is None or not isinstance(v, (int, float)):
            cell_failures.append(
                f"  MISSING  {check.label}: {check.sheet}!{check.cell} not found or non-numeric ({v!r})"
            )
            continue
        if abs(v - check.expected) > check.tolerance:
            cell_failures.append(
                f"  FAIL     {check.label}: got {v}, expected {check.expected}+-{check.tolerance}"
            )
            continue
        print(f"  OK CELL  {check.label}: {v:.4f}")

        if check.prose_patterns:
            prose_checked += 1
            matched = next((p for p in check.prose_patterns if re.search(p, prose)), None)
            if matched:
                print(f"  OK PROSE {check.label}: matched /{matched}/ ({check.section_hint})")
            else:
                prose_failures.append(
                    f"  PROSE    {check.label}: no match in index.md for "
                    f"{check.prose_patterns} ({check.section_hint})"
                )

    failures = cell_failures + prose_failures
    if failures:
        print()
        for msg in failures:
            print(msg)
        print(
            f"\nFAILED: {len(cell_failures)} cell + {len(prose_failures)} prose "
            f"({len(failures)} total of {len(CHECKS)} cell + {prose_checked} prose)"
        )
        sys.exit(1)

    print(
        f"\nPASSED: {len(CHECKS)} cell checks + {prose_checked} prose checks"
    )


if __name__ == "__main__":
    main()
