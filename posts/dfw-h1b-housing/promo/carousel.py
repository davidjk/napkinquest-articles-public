"""Instagram carousel for dfw-h1b-housing.

Emits 7 PNGs at 1080x1350 into ./carousel/. Every figure is pulled live from
the archived model (napkinquest-press/archive/dfw-h1b-housing/model.xlsx), so
the slides stay locked to the numbers the article quotes.
"""
from __future__ import annotations

from pathlib import Path

from napkinquest.carousel import (
    SIZE_SUBHEAD, bignum, cta_slide, divider, footer, label,
    new_slide, render, sans, serif,
)
from napkinquest.theme import ACCENT, INK, LOSS, MUTED, NAVY

HERE = Path(__file__).resolve().parent
OUT = HERE / "carousel"
MODEL = HERE.parents[3] / "napkinquest-press" / "archive" / "dfw-h1b-housing" / "model.xlsx"
TOTAL = 7
BODY = 17  # larger than SIZE_BODY for phone legibility
PAIR = 62  # focal-number size when two numbers share a slide

CELLS = {
    "edge_peak": ("Calculations", "D35"),    # Collin edge, 2022Q2
    "edge_now": ("Calculations", "G35"),     # Collin edge, 2026Q3
    "ai_2023": ("Inputs", "G5"),             # Collin Asian Indian purchases, 2023
    "ai_2025": ("Inputs", "I5"),             # ... 2025
    "ai_2024_chg": ("Calculations", "H9"),   # 2023 to 2024 change
    "fee_lost": ("Calculations", "B53"),     # Stage 0 lost purchases a year
    "ai_lost": ("Calculations", "B24"),      # Asian Indian purchases lost 2023-25
    "ai_12": ("Calculations", "B88"),        # Asian Indian, 12 counties, 2024-25
    "cn_12": ("Calculations", "B89"),        # Chinese, 12 counties, 2024-25
    "in_h1b": ("Inputs", "B78"),             # India-born share of FY24 H-1B approvals
    "cn_h1b": ("Inputs", "B79"),             # China-born share
}


def load_values() -> dict:
    import formulas
    import numpy as np

    sol = formulas.ExcelModel().loads(str(MODEL)).finish().calculate()
    out = {}
    for key, (sheet, cell) in CELLS.items():
        v = sol[f"'[{MODEL.name}]{sheet.upper()}'!{cell}"].value
        out[key] = float(v.flat[0] if isinstance(v, np.ndarray) else v)
    return out


V = load_values()


def pct(x: float) -> str:
    """-0.2753 -> '−28%' (true minus sign), 0.4286 -> '43%'."""
    s = f"{abs(x) * 100:.0f}%"
    return ("−" + s) if x < 0 else s


def num(x: float, nearest: int = 1) -> str:
    return f"{round(x / nearest) * nearest:,.0f}"


def slide_01_hook():
    fig = new_slide(url=True)
    serif(fig, 0.06, 0.80,
          "Did a $100,000\nH-1B visa fee\nsink North Texas\nhome prices?",
          size=50, color=INK)
    sans(fig, 0.06, 0.30,
         "Half the story holds up.\nThe mortgage data shows which half.",
         size=19, color=MUTED, style="italic")
    footer(fig, slide_num=1, slide_total=TOTAL, right="Swipe →")
    return fig


def slide_02_edge():
    fig = new_slide()
    label(fig, 0.5, 0.86, "Collin's price edge", ha="center")
    bignum(fig, 0.27, 0.66, pct(V["edge_peak"]), size=PAIR)
    sans(fig, 0.27, 0.565, "mid-2022", size=16, color=MUTED, ha="center")
    sans(fig, 0.5, 0.66, "→", size=46, color=MUTED, ha="center", va="center")
    bignum(fig, 0.73, 0.66, pct(V["edge_now"]), size=PAIR, color=LOSS)
    sans(fig, 0.73, 0.565, "late 2026", size=16, color=MUTED, ha="center")
    divider(fig, 0.15, 0.48, 0.70)
    sans(fig, 0.5, 0.43,
         "How much more a typical Collin County home\nis worth than one elsewhere in Dallas-Fort Worth.\nThe edge it rebuilt after 2020 is nearly gone.",
         size=BODY, color=INK, ha="center")
    footer(fig, slide_num=2, slide_total=TOTAL)
    return fig


def slide_03_buyers():
    fig = new_slide()
    label(fig, 0.5, 0.86, "One group of buyers", ha="center")
    bignum(fig, 0.5, 0.68, pct(V["ai_2025"] / V["ai_2023"] - 1), color=LOSS)
    sans(fig, 0.5, 0.56,
         "home-purchase mortgages to Asian Indian\nborrowers in Collin, 2023 to 2025",
         size=SIZE_SUBHEAD, color=INK, ha="center")
    divider(fig, 0.15, 0.44, 0.70)
    sans(fig, 0.5, 0.39,
         f"{num(V['ai_2023'])} purchases in 2023, {num(V['ai_2025'])} in 2025.\n"
         "Everyone else in Collin bought slightly more.",
         size=BODY, color=MUTED, ha="center")
    footer(fig, slide_num=3, slide_total=TOTAL)
    return fig


def slide_04_before_fee():
    fig = new_slide()
    label(fig, 0.5, 0.86, "Before the fee", ha="center")
    bignum(fig, 0.5, 0.68, "2024", color=NAVY)
    sans(fig, 0.5, 0.56,
         "is when the pullback started,\na year before the $100,000 fee",
         size=SIZE_SUBHEAD, color=INK, ha="center")
    divider(fig, 0.15, 0.44, 0.70)
    sans(fig, 0.5, 0.39,
         f"Asian Indian purchases in Collin fell {pct(V['ai_2024_chg']).lstrip(chr(0x2212))} in 2024.\n"
         "That year's drop came only in Sun Belt\ncounties where these buyers had surged.",
         size=BODY, color=MUTED, ha="center")
    footer(fig, slide_num=4, slide_total=TOTAL)
    return fig


def slide_05_too_small():
    fig = new_slide()
    label(fig, 0.5, 0.86, "Too small", ha="center")
    bignum(fig, 0.27, 0.66, num(V["fee_lost"], 10), size=PAIR, color=NAVY)
    sans(fig, 0.27, 0.565, "purchases a year\nthe fee could cost", size=15, color=MUTED, ha="center")
    sans(fig, 0.5, 0.66, "vs", size=28, color=MUTED, ha="center", va="center")
    bignum(fig, 0.73, 0.66, num(V["ai_lost"], 50), size=PAIR, color=LOSS)
    sans(fig, 0.73, 0.565, "purchases actually\nlost, 2023 to 2025", size=15, color=MUTED, ha="center")
    divider(fig, 0.15, 0.45, 0.70)
    sans(fig, 0.5, 0.40,
         "Back of the napkin, the fee hits only new\nworkers coming from abroad. The drop in\nCollin was nearly six times bigger.",
         size=BODY, color=INK, ha="center")
    footer(fig, slide_num=5, slide_total=TOTAL)
    return fig


def slide_06_twelve():
    fig = new_slide()
    label(fig, 0.5, 0.86, "Twelve counties, 2025", ha="center")
    bignum(fig, 0.27, 0.66, pct(V["ai_12"]), size=PAIR, color=LOSS)
    sans(fig, 0.27, 0.565, f"Asian Indian buyers\n{V['in_h1b'] * 100:.0f}% of H-1B approvals",
         size=15, color=MUTED, ha="center")
    bignum(fig, 0.73, 0.66, pct(V["cn_12"]), size=PAIR, color=NAVY)
    sans(fig, 0.73, 0.565, f"Chinese buyers\n~{V['cn_h1b'] * 100:.0f}% of H-1B approvals",
         size=15, color=MUTED, ha="center")
    divider(fig, 0.15, 0.45, 0.70)
    sans(fig, 0.5, 0.40,
         "In 2025 the drop reached every county we checked,\ncoastal tech hubs included, in step with each\ngroup's H-1B exposure. Other buyers held steady.",
         size=BODY, color=INK, ha="center")
    footer(fig, slide_num=6, slide_total=TOTAL)
    return fig


def slide_07_cta():
    return cta_slide(
        heading="Right buyers.\nWrong culprit.",
        blurb="The full napkin math: where the buyers came from,\nwhat hit them in 2025, and what the data can't see.",
        slide_num=TOTAL, slide_total=TOTAL,
    )


SLIDES = [
    ("01.png", slide_01_hook),
    ("02.png", slide_02_edge),
    ("03.png", slide_03_buyers),
    ("04.png", slide_04_before_fee),
    ("05.png", slide_05_too_small),
    ("06.png", slide_06_twelve),
    ("07.png", slide_07_cta),
]


def main() -> None:
    for p in render(SLIDES, OUT):
        print("wrote", p)


if __name__ == "__main__":
    main()
