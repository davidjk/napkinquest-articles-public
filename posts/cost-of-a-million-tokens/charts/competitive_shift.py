"""Competitive shift chart — slope chart showing pre vs post-announcement cost per million tokens.

The article's surprise: of the three frontier labs, only Anthropic improved after the
April/May 2026 deal cluster. OpenAI's cost-side multipliers didn't change, which makes
OpenAI the most exposed lab on a relative basis. Slope chart makes the movement (or
lack thereof) the visual story.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from _theme import apply_theme, apply_framework

OUT = Path(__file__).resolve().parent.parent / "assets" / "competitive-shift.png"

# Computed from the spreadsheet's multiplier model, lab-cash midpoint.
# Baseline lab: $154 ($7 train + $7 inf + $3 infra + $34 R&D + $103 capex).
# Google: 0.55 inference, 0.65 infra, 0.85 R&D, 0.7 capex → ~$114 (no change pre→post).
# Anthropic pre: 0.85 inference, 0.95 infra → ~$153; post: 0.72 inference, 0.85 infra, 0.85 capex → ~$137.
# OpenAI: all cost-side multipliers stay 1.0 pre→post → $154 (only distribution/CAC changed, not summed in cost).
LABS = [
    {"name": "Google", "pre": 114, "post": 114, "color": "#9da3aa"},
    {"name": "Anthropic", "pre": 153, "post": 137, "color": sns.color_palette("viridis", n_colors=5)[3]},
    {"name": "OpenAI", "pre": 154, "post": 154, "color": "#d65a4e"},
]

X_PRE = 0
X_POST = 1


def main() -> None:
    apply_theme()
    fig, ax = plt.subplots(figsize=(10, 5))

    for lab in LABS:
        ax.plot(
            [X_PRE, X_POST],
            [lab["pre"], lab["post"]],
            color=lab["color"],
            linewidth=3.5,
            marker="o",
            markersize=11,
            markerfacecolor=lab["color"],
            markeredgecolor="white",
            markeredgewidth=2,
        )
        # Right-side label: name + post value
        ax.text(
            X_POST + 0.04,
            lab["post"],
            f"  {lab['name']}  ${lab['post']}",
            va="center",
            ha="left",
            color=lab["color"],
            weight="bold",
            fontsize=13,
        )

    # Highlight Anthropic's drop with a delta annotation
    anthropic = LABS[1]
    mid_x = (X_PRE + X_POST) / 2
    mid_y = (anthropic["pre"] + anthropic["post"]) / 2
    ax.annotate(
        "−$16 / −11%",
        xy=(mid_x, mid_y),
        xytext=(mid_x, mid_y - 12),
        ha="center",
        color=anthropic["color"],
        weight="bold",
        fontsize=12,
    )

    ax.set_xticks([X_PRE, X_POST])
    ax.set_xticklabels(["Early 2026", "May 2026"])
    ax.set_ylabel("")
    ax.set_xlim(X_PRE - 0.05, X_POST + 0.28)
    ax.set_ylim(108, 162)
    ax.spines["bottom"].set_color("#888")

    apply_framework(
        fig, ax,
        title="Anthropic dropped 11%. OpenAI's diversification lands years later.",
        subtitle="$ per million output tokens, lab-cash midpoint",
        source="Source: cost-of-a-million-tokens spreadsheet model, May 2026",
        rule_color=sns.color_palette("viridis", n_colors=5)[3],
        value_axis="y",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
