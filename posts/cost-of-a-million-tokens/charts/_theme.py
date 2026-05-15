"""Shared chart theme for cost-of-a-million-tokens.

Charts use an Economist-inspired structural framework (accent rule, tiered title
block, source caption, minimal chrome) with a viridis-derived palette. Convention
matches src/napkinquest/chart.py (whitegrid + talk context).
"""
from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Rectangle

ACCENT = "#3dae7b"  # viridis-derived green, used for the accent rule by default


def apply_theme() -> None:
    sns.set_theme(style="white", context="talk")
    plt.rcParams.update(
        {
            "axes.labelweight": "regular",
            "axes.labelsize": 11,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.spines.left": False,
            "axes.edgecolor": "#888",
            "xtick.color": "#666",
            "ytick.color": "#222",
            "xtick.labelsize": 10.5,
            "ytick.labelsize": 12,
            "figure.dpi": 200,
            # Inter sans for body / labels (has full italic + weight variants as individual OTF files).
            # Georgia serif for the title via apply_framework (has bold + italic as proper TTFs).
            "font.family": "sans-serif",
            "font.sans-serif": ["Inter", "Helvetica Neue", "Helvetica", "DejaVu Sans"],
            "font.serif": ["Georgia", "Charter", "DejaVu Serif"],
        }
    )


def palette(n: int) -> list:
    """Return n viridis colors. Designed for ordered stacks: smallest → darkest, largest → brightest."""
    return sns.color_palette("viridis", n_colors=n)


def apply_framework(
    fig,
    ax,
    *,
    title: str,
    subtitle: str | None = None,
    source: str | None = None,
    rule_color: str = ACCENT,
    value_axis: str = "x",
    left_pad: float = 0.08,
) -> None:
    """Apply the Economist-inspired chart framework.

    Adds an accent rule at top-left, bold title below, optional italic subtitle,
    optional italic source caption at bottom-left. Adjusts axes position so the
    title block sits above the chart, source below. Adds subtle gridlines on the
    value axis only.

    Args:
        value_axis: "x" for horizontal bar charts (value scale on x), "y" for
            line/slope charts and vertical bar charts. Controls which axis
            gets the subtle gridlines.
    """
    LEFT_FIG = 0.06
    LEFT_AX = left_pad
    RIGHT_AX = 0.96
    TITLE_Y = 0.92
    SUBTITLE_Y = 0.85
    SOURCE_Y = 0.04
    RULE_Y = 0.965
    RULE_WIDTH = 0.05
    RULE_HEIGHT = 0.012

    rule = Rectangle(
        (LEFT_FIG, RULE_Y),
        RULE_WIDTH,
        RULE_HEIGHT,
        transform=fig.transFigure,
        color=rule_color,
        clip_on=False,
    )
    fig.add_artist(rule)

    # Title in Charter serif for editorial weight; subtitle and source in Avenir sans italic.
    fig.text(
        LEFT_FIG, TITLE_Y, title,
        ha="left", va="top",
        fontsize=19, weight="bold", color="#111",
        family="serif",
    )

    if subtitle:
        fig.text(
            LEFT_FIG, SUBTITLE_Y, subtitle,
            ha="left", va="top",
            fontsize=12, style="italic", color="#666",
            family="sans-serif",
        )

    if source:
        fig.text(
            LEFT_FIG, SOURCE_Y, source,
            ha="left", va="bottom",
            fontsize=10, style="italic", color="#999",
            family="sans-serif",
        )

    top = 0.78 if subtitle else 0.86
    bottom = 0.14 if source else 0.10
    ax.set_position([LEFT_AX, bottom, RIGHT_AX - LEFT_AX, top - bottom])

    if value_axis == "x":
        ax.grid(axis="x", color="#e4e4e4", linewidth=0.8, zorder=0)
        ax.grid(axis="y", visible=False)
    else:
        ax.grid(axis="y", color="#e4e4e4", linewidth=0.8, zorder=0)
        ax.grid(axis="x", visible=False)
