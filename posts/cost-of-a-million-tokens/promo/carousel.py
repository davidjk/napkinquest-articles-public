"""Instagram carousel slides for cost-of-a-million-tokens.

Emits 9 PNGs at 1080x1350 (Instagram portrait 4:5) into ./carousel/.
Each slide is a single-finding card with one defensible number, in the same
Economist-inspired aesthetic as the article charts (Georgia serif title block,
green accent rule, viridis palette).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

# Theme tokens — match the article's charts/_theme.py so the carousel reads
# as the same publication. Inlined here so the promo bundle is self-contained
# and can live in the private press repo while charts/ stays with the article.
ACCENT = "#3dae7b"  # viridis-derived green

def palette(n: int) -> list:
    return sns.color_palette("viridis", n_colors=n)

OUT = Path(__file__).resolve().parent / "carousel"

# Page geometry: 1080x1350 px @ 150 dpi → 7.2 x 9.0 inches.
W_IN, H_IN = 7.2, 9.0
DPI = 150

# Color tokens.
INK = "#111111"
MUTED = "#5a5a5a"
SUBTLE = "#8a8a8a"
HAIRLINE = "#dcdcdc"
CAPEX = palette(5)[3]      # viridis green — protagonist for cost-stack
INFERENCE = "#1f3268"      # navy — the "wrong answer" framing in the article
LOSS = "#b3322c"           # muted red for negative/loss callouts
BG = "#ffffff"

# Font-size tokens (points at 150 dpi).
SIZE_BIGNUM = 110          # for centered focal numbers like "$154", "−11%"
SIZE_BIGNUM_NARROW = 130   # for short focal numbers like "$7"
SIZE_HEADLINE = 32         # serif bold claim block
SIZE_SUBHEAD = 18          # supporting line under big number
SIZE_BODY = 14             # supporting paragraph
SIZE_LABEL = 11            # green tracked-out section label


# ---------------------------------------------------------------------------
# Shared scaffolding
# ---------------------------------------------------------------------------

def new_slide():
    """Return fig for a portrait carousel slide with NQ scaffolding drawn."""
    fig = plt.figure(figsize=(W_IN, H_IN), dpi=DPI, facecolor=BG)
    fig.add_artist(Rectangle((0.06, 0.955), 0.10, 0.010,
                             transform=fig.transFigure,
                             color=ACCENT, clip_on=False))
    fig.text(0.06, 0.935, "N A P K I N Q U E S T",
             ha="left", va="top",
             fontsize=10, weight="bold", color=INK, family="sans-serif")
    return fig


def footer(fig, *, slide_num: int, slide_total: int, right: str = ""):
    fig.text(0.06, 0.035, f"{slide_num} / {slide_total}",
             ha="left", va="bottom",
             fontsize=10, color=SUBTLE, family="sans-serif", style="italic")
    if right:
        fig.text(0.94, 0.035, right,
                 ha="right", va="bottom",
                 fontsize=10, color=SUBTLE, family="sans-serif", style="italic")


def serif(fig, x, y, text, *, size, color=INK, ha="left", va="top", weight="bold"):
    return fig.text(x, y, text, ha=ha, va=va,
                    fontsize=size, weight=weight, color=color, family="serif")


def sans(fig, x, y, text, *, size, color=MUTED, ha="left", va="top",
         style="normal", weight="regular"):
    return fig.text(x, y, text, ha=ha, va=va,
                    fontsize=size, weight=weight, color=color,
                    family="sans-serif", style=style)


def label(fig, x, y, text, *, color=ACCENT, size=SIZE_LABEL, ha="left", va="top"):
    """Small caps-style section label."""
    return fig.text(x, y, text.upper(), ha=ha, va=va,
                    fontsize=size, weight="bold", color=color,
                    family="sans-serif")


def bignum(fig, x, y, text, *, size=SIZE_BIGNUM, color=INK, ha="center", va="center"):
    """Centered focal number, serif bold."""
    return fig.text(x, y, text, ha=ha, va=va,
                    fontsize=size, weight="bold", color=color, family="serif")


# ---------------------------------------------------------------------------
# Slides
# ---------------------------------------------------------------------------

def slide_01_hook():
    fig = new_slide()
    serif(fig, 0.06, 0.80,
          "What does\na million\ntokens cost\na frontier\nAI lab?",
          size=56, color=INK)
    sans(fig, 0.06, 0.22,
         "Two numbers. Two scenarios.\nA napkin-math read on the $200B AI commitments.",
         size=17, color=MUTED, style="italic")
    footer(fig, slide_num=1, slide_total=9, right="Swipe →")
    return fig


def slide_02_number():
    fig = new_slide()

    label(fig, 0.5, 0.85, "Lab cash basis", ha="center")
    bignum(fig, 0.5, 0.74, "$154", size=120)
    sans(fig, 0.5, 0.64, "per million output tokens", size=18, color=MUTED, ha="center")
    sans(fig, 0.5, 0.605,
         "What frontier labs spend out of pocket.\nThe basis behind OpenAI's $5B 2024 loss.",
         size=14, color=MUTED, ha="center")

    fig.add_artist(Rectangle((0.30, 0.515), 0.40, 0.0015,
                             transform=fig.transFigure, color=HAIRLINE, clip_on=False))

    label(fig, 0.5, 0.485, "Full economic basis", color=CAPEX, ha="center")
    bignum(fig, 0.5, 0.375, "$253", size=120)
    sans(fig, 0.5, 0.275, "per million output tokens", size=18, color=MUTED, ha="center")
    sans(fig, 0.5, 0.24,
         "Loaded with the capex hyperscaler partners bear.\nThe basis the $200B commitments need to pencil.",
         size=14, color=MUTED, ha="center")
    footer(fig, slide_num=2, slide_total=9)
    return fig


def slide_03_stack():
    """Horizontal stacked bar, inline labels in wide segments, callouts above slivers."""
    fig = new_slide()
    serif(fig, 0.06, 0.86, "Five layers.\nOne dominates.", size=42, color=INK)
    sans(fig, 0.06, 0.69,
         "Cost per million output tokens, lab-cash midpoint",
         size=14, color=MUTED, style="italic")

    bar_left = 0.06
    bar_right = 0.94
    bar_y = 0.50
    bar_height = 0.06

    LAYERS = [
        ("Training",        7,  "#cfd2d6"),
        ("Inference",       7,  INFERENCE),
        ("Infrastructure",  3,  "#cfd2d6"),
        ("R&D / people",    36, "#cfd2d6"),
        ("Capex",          103, CAPEX),
    ]
    total = sum(v for _, v, _ in LAYERS)

    x = bar_left
    span = bar_right - bar_left
    centers = []
    for name, value, color in LAYERS:
        w = span * value / total
        fig.add_artist(Rectangle((x, bar_y), w, bar_height,
                                 transform=fig.transFigure,
                                 facecolor=color, edgecolor="white", linewidth=1.5,
                                 clip_on=False))
        centers.append((name, value, color, x + w / 2, w))
        x += w

    # Inline labels for the two largest segments (R&D, Capex).
    _, _, _, cx_rd, _ = centers[3]
    fig.text(cx_rd, bar_y + bar_height / 2, "$36",
             ha="center", va="center",
             fontsize=18, weight="bold", color=INK, family="serif")
    fig.text(cx_rd, bar_y + bar_height + 0.012, "R&D",
             ha="center", va="bottom",
             fontsize=11, color=MUTED, family="sans-serif")

    _, _, _, cx_cx, _ = centers[4]
    fig.text(cx_cx, bar_y + bar_height / 2, "$103",
             ha="center", va="center",
             fontsize=32, weight="bold", color="white", family="serif")
    fig.text(cx_cx, bar_y + bar_height + 0.012, "Capex amortization",
             ha="center", va="bottom",
             fontsize=12, weight="bold", color=CAPEX, family="sans-serif")

    # Single callout below the three slivers: bracket + leader + grouped label.
    cx_inf = centers[1][3]
    sliver_left_edge = centers[0][3] - centers[0][4] / 2
    sliver_right_edge = centers[2][3] + centers[2][4] / 2
    bracket_y = bar_y - 0.010
    # Horizontal bracket spanning the three slivers.
    fig.add_artist(Rectangle((sliver_left_edge, bracket_y - 0.001),
                             sliver_right_edge - sliver_left_edge, 0.001,
                             transform=fig.transFigure,
                             facecolor=MUTED, edgecolor="none", clip_on=False))
    # L-shaped leader: down from bracket center, then horizontal to label anchor.
    label_x = 0.20
    fig.add_artist(Rectangle((cx_inf - 0.0005, bracket_y - 0.020), 0.001, 0.020,
                             transform=fig.transFigure,
                             facecolor=MUTED, edgecolor="none", clip_on=False))
    fig.add_artist(Rectangle((cx_inf, bracket_y - 0.021),
                             label_x - cx_inf, 0.001,
                             transform=fig.transFigure,
                             facecolor=MUTED, edgecolor="none", clip_on=False))
    sans(fig, label_x + 0.005, bar_y - 0.027,
         "Training $7 · Inference $7 · Infra $3",
         size=11, color=MUTED, ha="left", va="top")
    sans(fig, label_x + 0.005, bar_y - 0.050,
         "(the popular 'GPU bill' framing lives in 'Inference')",
         size=10, color=INFERENCE, ha="left", va="top", style="italic")

    # Takeaway block at the bottom.
    serif(fig, 0.06, 0.31,
          "Capex eats 2/3.\nInference eats 1/22.",
          size=30, color=INK)
    sans(fig, 0.06, 0.13,
         "The popular 'GPU bill is the cost' framing\nis off by an order of magnitude.",
         size=14, color=MUTED)
    footer(fig, slide_num=3, slide_total=9)
    return fig


def slide_04_inference():
    fig = new_slide()
    label(fig, 0.5, 0.83, "Inference compute, midpoint", ha="center")
    bignum(fig, 0.5, 0.66, "$7", size=200, color=INFERENCE)
    sans(fig, 0.5, 0.50, "per million output tokens",
         size=20, color=MUTED, ha="center")

    serif(fig, 0.06, 0.40,
          "The GPU bill isn't\nwhere the money goes.",
          size=32, color=INK)
    sans(fig, 0.06, 0.21,
         "Capex amortization is $103. R&D is $36. Training $7.\nThe headline number lives in the buildout,\nnot the chips that run the queries.",
         size=14, color=MUTED)
    footer(fig, slide_num=4, slide_total=9)
    return fig


def slide_05_subsidy():
    fig = new_slide()
    label(fig, 0.5, 0.83, "Median $20 / month subscription", ha="center")
    bignum(fig, 0.5, 0.66, "−$18", size=130, color=LOSS)
    sans(fig, 0.5, 0.50, "per month at full-economic cost",
         size=20, color=MUTED, ha="center")

    serif(fig, 0.06, 0.40,
          "Investors are subsidizing\nthe consumer flat rate.",
          size=30, color=INK)
    sans(fig, 0.06, 0.21,
         "Light users (~130 queries / month) clear cost.\nThe median user is modestly underwater on cash.\nPower users compound the loss fast.",
         size=14, color=MUTED)
    footer(fig, slide_num=5, slide_total=9)
    return fig


def slide_06_google():
    fig = new_slide()
    label(fig, 0.5, 0.83, "Google's cost per token", ha="center")
    bignum(fig, 0.5, 0.66, "~30%", size=130, color=CAPEX)
    sans(fig, 0.5, 0.50, "lower than the standalone-lab baseline",
         size=18, color=MUTED, ha="center")

    serif(fig, 0.06, 0.40,
          "TPUs. End-to-end stack.\nDistribution at zero CAC.",
          size=30, color=INK)
    sans(fig, 0.06, 0.21,
         "Self-funded from a $260B+ ad business.\nDecades of search and YouTube data.\nThe cost gap holds across every layer.",
         size=14, color=MUTED)
    footer(fig, slide_num=6, slide_total=9)
    return fig


def slide_07_anthropic():
    fig = new_slide()
    label(fig, 0.5, 0.83, "Anthropic, after April", ha="center")
    bignum(fig, 0.5, 0.66, "−11%", size=140, color=CAPEX)
    sans(fig, 0.5, 0.50, "cost per token, post-deal",
         size=20, color=MUTED, ha="center")

    serif(fig, 0.06, 0.40,
          "Three deals.\nThree silicon stacks.",
          size=32, color=INK)
    sans(fig, 0.06, 0.21,
         "From Google: $40B and 5GW of TPUs.\nFrom Amazon: $25B and 5GW of Trainium.\nxAI's Colossus 1: 220k+ Nvidia GPUs.\nFrom single-stack tenant to multi-stack hedge.",
         size=14, color=MUTED)
    footer(fig, slide_num=7, slide_total=9)
    return fig


def slide_08_demand():
    fig = new_slide()
    label(fig, 0.5, 0.83, "What the commitments price in", ha="center")
    bignum(fig, 0.5, 0.66, "~2×", size=160, color=INK)
    sans(fig, 0.5, 0.50, "the tokens the industry serves today",
         size=20, color=MUTED, ha="center")

    serif(fig, 0.06, 0.40,
          "40 million paying seats.",
          size=32, color=INK)
    sans(fig, 0.06, 0.31,
         "Roughly California's population, at heavy-use intensity.",
         size=14, color=MUTED, style="italic")
    sans(fig, 0.06, 0.22,
         "Or: 1.7M developers using AI the way a Claude Code\nuser does today. That's the entire US software\ndeveloper workforce.",
         size=14, color=MUTED)
    footer(fig, slide_num=8, slide_total=9)
    return fig


def slide_09_scenarios():
    fig = new_slide()
    serif(fig, 0.06, 0.87, "Two scenarios.", size=44, color=INK)
    sans(fig, 0.06, 0.785,
         "The math closes in one.",
         size=17, color=MUTED, style="italic")

    # Scenario A — green sidebar.
    fig.add_artist(Rectangle((0.06, 0.575), 0.006, 0.13,
                             transform=fig.transFigure,
                             color=CAPEX, clip_on=False))
    label(fig, 0.10, 0.70, "Scenario A. Demand compounds.", color=CAPEX, size=12)
    sans(fig, 0.10, 0.665,
         "All three frontier labs find profitable scale.\nThe 1.9x token growth multiple clears.",
         size=14, color=INK)

    # Scenario B — red sidebar.
    fig.add_artist(Rectangle((0.06, 0.39), 0.006, 0.13,
                             transform=fig.transFigure,
                             color=LOSS, clip_on=False))
    label(fig, 0.10, 0.515, "Scenario B. Demand stalls.", color=LOSS, size=12)
    sans(fig, 0.10, 0.480,
         "Two labs hold frontier-class economics.\nThe third gets restructured. Wind-down,\nasset sale, or CSP absorption.",
         size=14, color=INK)

    # CTA section.
    fig.add_artist(Rectangle((0.06, 0.33), 0.88, 0.0015,
                             transform=fig.transFigure, color=HAIRLINE, clip_on=False))
    serif(fig, 0.06, 0.27, "Full breakdown.", size=36, color=INK)
    sans(fig, 0.06, 0.175, "Link in bio.", size=17, color=MUTED, style="italic")
    sans(fig, 0.06, 0.115,
         "Spreadsheet model, sources, the chart of who's most cost-exposed,\nand the diagnostic ratios for which scenario plays out.",
         size=12, color=MUTED)
    footer(fig, slide_num=9, slide_total=9)
    return fig


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

SLIDES = [
    ("01-hook.png",        slide_01_hook),
    ("02-the-number.png",  slide_02_number),
    ("03-cost-stack.png",  slide_03_stack),
    ("04-inference.png",   slide_04_inference),
    ("05-subsidy.png",     slide_05_subsidy),
    ("06-google.png",      slide_06_google),
    ("07-anthropic.png",   slide_07_anthropic),
    ("08-demand.png",      slide_08_demand),
    ("09-scenarios.png",   slide_09_scenarios),
]


def main() -> None:
    sns.set_theme(style="white", context="talk")
    plt.rcParams.update({
        "font.family": "sans-serif",
        "font.sans-serif": ["Inter", "Helvetica Neue", "Helvetica", "DejaVu Sans"],
        "font.serif": ["Georgia", "Charter", "DejaVu Serif"],
        # Disable math-mode parsing globally so '$154' renders literally instead
        # of getting picked up as math delimiters.
        "text.parse_math": False,
    })
    OUT.mkdir(parents=True, exist_ok=True)
    for fname, builder in SLIDES:
        fig = builder()
        path = OUT / fname
        fig.savefig(path, dpi=DPI, facecolor=BG, bbox_inches=None, pad_inches=0)
        plt.close(fig)
        print(f"Wrote {path}")


if __name__ == "__main__":
    main()
