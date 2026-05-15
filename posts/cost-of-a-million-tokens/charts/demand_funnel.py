"""Demand funnel chart — anchors the article's implied user counts (19.8M heavy users,
40M paying seats) against today's developer-pool and US-state populations.

The article's finding is that the demand bet doesn't require broad office-worker
conversion. The implied user counts are within the global developer pool by
headcount (used here as a scale reference, not a claim about who the heavy users
will be) and correspond to recognizable population scales (NY State, California).
Chart makes both anchors visible side-by-side.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from _theme import apply_theme, apply_framework

OUT = Path(__file__).resolve().parent.parent / "assets" / "demand-funnel.png"

ACCENT = sns.color_palette("viridis", n_colors=5)[3]
NEUTRAL = "#cfd2d6"

# Sorted small → large for visual ascent.
BARS = [
    {"label": "US developers", "value": 1.7, "anchor": "BLS, 2024", "color": NEUTRAL, "kind": "today"},
    {"label": "Implied heavy users", "value": 19.8, "anchor": "≈ New York State pop. (19.5M)", "color": ACCENT, "kind": "implied"},
    {"label": "Implied paying seats", "value": 40.0, "anchor": "≈ California pop. (39M)", "color": ACCENT, "kind": "implied"},
    {"label": "Global developers", "value": 47.0, "anchor": "SlashData, 2025", "color": NEUTRAL, "kind": "today"},
]


def main() -> None:
    apply_theme()
    fig, ax = plt.subplots(figsize=(10, 5))

    labels = [b["label"] for b in BARS]
    values = [b["value"] for b in BARS]
    colors = [b["color"] for b in BARS]

    bars = ax.barh(labels, values, color=colors, edgecolor="white", linewidth=1.5, height=0.62)

    for bar, b in zip(bars, BARS):
        x = bar.get_width()
        y = bar.get_y() + bar.get_height() / 2
        # Value + anchor label, color-coded by bar kind
        text_color = "#444" if b["kind"] == "today" else "#1d6f59"
        ax.text(
            x + 0.7,
            y,
            f"{b['value']:g}M — {b['anchor']}",
            va="center",
            ha="left",
            color=text_color,
            fontsize=12,
            weight="bold" if b["kind"] == "implied" else "regular",
        )

    ax.set_xlim(0, 64)
    ax.set_xlabel("")
    ax.invert_yaxis()
    ax.spines["bottom"].set_color("#888")

    apply_framework(
        fig, ax,
        title="Demand bet vs global developer pool",
        subtitle="Industry-implied user counts vs developer-pool benchmarks, millions",
        source="Sources: BLS (2024), SlashData (2025); cost-of-a-million-tokens model",
        rule_color=ACCENT,
        value_axis="x",
        left_pad=0.18,  # extra room for long y-axis category labels
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
