"""Cost stack chart — single bar, lab-cash basis, calling out the inference-vs-capex contrast.

The popular framing is that "the GPU bill" (inference) is the cost of AI. The model shows
inference is $7/M while capex amortization is $103/M. Chart accents those two segments
specifically so the contrast is unmissable; the other layers fade to neutral gray.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from _theme import apply_theme, apply_framework

OUT = Path(__file__).resolve().parent.parent / "assets" / "cost-stack.png"

# Lab-cash basis, midpoint. Article totals: $154 = $7 + $7 + $3 + $34 + $103.
INFERENCE_ACCENT = "#1f3268"  # navy — the "wrong answer" framing
CAPEX_ACCENT = sns.color_palette("viridis", n_colors=5)[3]  # viridis green — the real story

LAYERS = [
    ("Training", 7, "#cfd2d6"),
    ("Inference", 7, INFERENCE_ACCENT),
    ("Infrastructure", 3, "#cfd2d6"),
    ("R&D / people / data", 34, "#cfd2d6"),
    ("Capex amortization", 103, CAPEX_ACCENT),
]
TOTAL = sum(v for _, v, _ in LAYERS)  # 154


def main() -> None:
    apply_theme()

    fig, ax = plt.subplots(figsize=(10, 5))

    left = 0
    for name, value, color in LAYERS:
        ax.barh([0], [value], left=left, color=color, edgecolor="white", linewidth=1.5, height=0.5, zorder=3)
        left += value

    inference_center = 7 + 7 / 2
    capex_start = 7 + 7 + 3 + 34
    capex_center = capex_start + 103 / 2

    ax.annotate(
        "Inference: $7\nthe \"GPU bill\" framing",
        xy=(inference_center, 0.25),
        xytext=(inference_center, 0.75),
        ha="center",
        fontsize=12,
        color=INFERENCE_ACCENT,
        weight="bold",
        arrowprops=dict(arrowstyle="-", color=INFERENCE_ACCENT, lw=1.2, shrinkA=0, shrinkB=2),
    )

    ax.annotate(
        "Capex amortization: $103\ntwo-thirds of the cost",
        xy=(capex_center, -0.25),
        xytext=(capex_center, -0.75),
        ha="center",
        fontsize=12,
        color=CAPEX_ACCENT,
        weight="bold",
        arrowprops=dict(arrowstyle="-", color=CAPEX_ACCENT, lw=1.2, shrinkA=0, shrinkB=2),
    )

    ax.text(TOTAL - 2, 0, f"${TOTAL}/M", va="center", ha="right", weight="bold", fontsize=14, color="white")

    ax.set_xlim(0, TOTAL * 1.05)
    ax.set_ylim(-1.05, 1.05)
    ax.set_yticks([])
    ax.set_xlabel("")
    ax.spines["bottom"].set_color("#888")

    apply_framework(
        fig, ax,
        title="The GPU bill isn't the cost. Capex is.",
        subtitle="Cost per million output tokens, lab-cash basis, midpoint scenario",
        source="Source: cost-of-a-million-tokens spreadsheet model, May 2026",
        rule_color=CAPEX_ACCENT,
        value_axis="x",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(OUT)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
