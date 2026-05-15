# Chart design review: cost-stack.png

**Chart:** assets/cost-stack.png
**Article:** index.md
**Generated:** 2026-05-13T12:16:54Z
**Reviewer:** chart-designer-critic

> This file is reference material — fixes live in the chart script (typically `charts/<chart_stem>.py`), not in the article markdown. There is no automated processor for chart design reviews; the writer applies findings by hand. Task-list markers (`[x]` addressed, `[ ]` open) are informational.

## Findings

- [ ] **1. [IMPORTANT] Chart shows lab-cash basis only; the article's central claim is a dual-basis story**

  **Where:** the entire chart — one bar totaling $154/M with no $253 reference, plus the subtitle ("lab-cash basis, midpoint scenario") which acknowledges the single basis but does nothing about it.
  **Issue:** The article's opening frames a dual answer: $154 on lab cash (today's headline losses) and $253 on full economic (what the $200B commitments need to pencil). The phrase "the $99 gap" between the two bases is doing real load-bearing work in the rest of the piece — the demand-doubling math, the consolidation argument, and the "who's most cost-exposed" finding all key off the full-economic basis. A reader who sees the chart, reads "$154/M," and skims onward walks away with one number when the article spends three paragraphs setting up two. Cairo: the chart must visualize the article's claim, not just one slice of the underlying model. This is the chart immediately under the section "The cost stack: five layers, one dominates," which is exactly where the dual basis lands in the prose.
  **Suggested redesign:** add a second stacked bar directly beneath the first for the full-economic basis ($253/M), broken into the same five layers but with the additional hyperscaler-borne capex sitting as an extended capex segment. Same accent treatment (capex green, inference navy, others gray). The two bars side by side make the $99 delta visible without prose. Alternative if a single bar must stay: extend the x-axis to 260, draw a dashed vertical "$253 full economic" reference line beyond the $154 bar end, and label it. The pair-of-bars version is stronger because it preserves layer-by-layer comparison.

- [ ] **2. [IMPORTANT] Three of five cost layers are unlabeled in place; the contiguous gray block reads as one segment, not three**

  **Where:** the left half of the bar — Training ($7, gray), Infrastructure ($3, gray), and R&D ($34, gray) share the same gray fill with white 1.5pt separators that disappear at the slim widths. From the rendered image, the gray-Training, navy-Inference, gray-Infrastructure, gray-R&D sequence reads as roughly: small-gray, small-navy, one-long-gray. Two of the five layers (Training $7 sliver and Infrastructure $3 sliver) are functionally invisible as distinct shapes.
  **Issue:** Knaflic: every segment the writer spends prose space on should be findable in the chart. The article devotes a full paragraph each to Training, Infrastructure, and R&D — Training is $7, Infrastructure is the article-named "smallest of the five layers" at $3, R&D is $36 (the chart shows $34, an internal rounding mismatch worth noting). A reader cannot count five layers in the chart. They see "capex, inference, and a gray block." The chart is hiding three of the five layers the section header promises. Tufte: minimize the round-trips — but there's no legend at all here, so the reader has no path to identify the gray segments. The chart structurally under-delivers the "five layers" claim its own section header sets up.
  **Suggested redesign:** label each segment in place. For the three gray segments, place each layer name and dollar value directly above (or in, for R&D which is wide enough) its segment, with a thin leader line if the segment is too narrow to hold text. Training and Infrastructure will need leaders pointing to their slivers; R&D ($34) is wide enough to hold "R&D $34" inline. Keep the existing accent annotations on Inference and Capex as the larger callouts. This converts the chart from "two findings, three mysteries" to "five labeled layers with two accented."

- [ ] **3. [IMPORTANT] Inference and Training are identical widths but only Inference is identifiable; Training reads as a leading-edge sliver of unknown meaning**

  **Where:** the leftmost two segments. Training ($7, gray) and Inference ($7, navy) are visually identical-width blocks immediately adjacent. The Inference annotation arrow points to the navy block, leaving Training as an unlabeled gray sliver at x=0–7 that the reader cannot place against the cost layers.
  **Issue:** The article's contrast is "inference is small, capex dominates" — and the chart accents inference for that contrast. But by accenting Inference against an immediately-adjacent identically-sized but unlabeled Training segment, the chart implicitly asks the reader to recognize there are two $7 segments without telling them what the other one is. The leftmost segment is the first thing the eye lands on after the title. It should be either labeled, or moved out of the leading position. The chart is also doing internal work — the visual equivalence of Training and Inference is a finding (training and inference cost the same, both small) the chart could be making explicit, but currently leaves implicit and unreadable.
  **Suggested redesign:** label Training in place ("Training $7"). Optionally reorder so the contrast pair (Inference and Capex) bracket the rest: e.g., Inference at the left, then R&D, Infrastructure, Training, with Capex at the right — but reordering trades the natural cost-stack reading for a contrast emphasis, so the inline label is the lower-risk fix.

- [ ] **4. [IMPORTANT] Subtitle states the basis but does not deliver context the title needs**

  **Where:** the subtitle line ("Cost per million output tokens, lab-cash basis, midpoint scenario").
  **Issue:** The title carries the finding ("The GPU bill isn't the cost. Capex is.") and the subtitle currently does a fine job naming units and basis. But the article's actual claim is sharper than the title carries: the GPU bill is small, capex is two-thirds, AND there's a second basis that pushes the total to $253. The subtitle has space to anchor the second number for the reader skimming only the chart. Right now the chart's three-second takeaway is "capex dominates at $154/M." The article's three-second takeaway is "capex dominates, and there are two answers: $154 and $253."
  **Suggested redesign:** if Finding 1's two-bar redesign is adopted, the current subtitle works as-is. If only the single bar remains, extend the subtitle: "Cost per million output tokens, midpoint scenario. Lab-cash basis $154/M; full-economic basis $253/M." Then the chart at least names both numbers even if only one is visualized.

- [ ] **5. [NICE-TO-HAVE] R&D layer value on the chart ($34) does not match the value in prose ($36)**

  **Where:** the script's `LAYERS` list assigns R&D = 34; the article body says "this layer runs about $36 per million output tokens at midpoint" and the chart's segments sum to $154, matching the article total.
  **Issue:** Not a visual-design issue per se, but a chart-internal-consistency issue worth surfacing because the chart is the public-facing number. The five article values are 7 + 7 + 3 + 36 + 103 = 156, not 154; the chart silently resolves the rounding by setting R&D to 34. The reader looking up the R&D paragraph and then reading the chart will see "$36" in prose and "$34" if the chart labels the segment per Finding 2. Internal consistency is one of the things that makes the writer's numbers feel defensible.
  **Suggested redesign:** decide on a single value (35 splits the difference, 36 matches the prose; either resolves the gap) and apply it both in `LAYERS` and in the article paragraph. The total will round to $154 either way given the rest of the rounding.

- [ ] **6. [NICE-TO-HAVE] $154/M label sits inside the green segment in white; readable, but inconsistent with the rest of the chart's typography**

  **Where:** the bold white "$154/M" label inside the right end of the green Capex segment.
  **Issue:** It works at this size but is the only inverted-color label in the chart, and the only label rendered against a color fill rather than against the figure background. If Finding 1's two-bar redesign happens, each bar needs an end-of-bar total label and consistency matters more. Currently the white-on-green creates a small visual hot spot that competes with the Capex annotation below the bar (also green, bold, larger).
  **Suggested redesign:** move "$154/M" to the right of the bar end (outside the bar, against the figure background, in dark text matching the axis tick color). This puts every label on the same background and frees the bar interior to carry just the encoded data. With the bar now ending around x=154 and the x-axis going to 160, there is just enough room. If Finding 1's two-bar redesign is adopted, place "$154/M" and "$253/M" both at the right end of their respective bars in dark text, consistently.

## Chart-question fit

The chart's takeaway: capex amortization is two-thirds of a frontier lab's cost per million tokens, while inference (the popular "GPU bill" framing) is a small fraction.
The article's central claim about this number: there are two cost answers — $154 on lab cash and $253 on full economic — and within either basis, capex dominates while inference is small.
Fit assessment: the chart fits the within-basis claim cleanly and delivers it in three seconds, but visualizes only the lab-cash half of the article's dual-basis story; the $253 figure that the rest of the article keys off (demand math, consolidation argument, who's most cost-exposed) is absent from the chart. Filed as Finding 1.

---

**Findings:** 0 CRITICAL, 4 IMPORTANT, 2 NICE-TO-HAVE
**Top redesign:** add a second stacked bar for the full-economic basis ($253/M) directly below the lab-cash bar, with the five layers labeled in place on both bars, so the chart carries the dual-basis finding the rest of the article keys off and so the reader can count and identify all five layers without a legend.
**Process notes:** Read napkinquest-voice SKILL.md; read article in full; read chart script `articles/cost-of-a-million-tokens/charts/cost_stack.py` and shared `_theme.py`. Two sibling charts exist in `assets/` (`competitive-shift.png`, `demand-funnel.png`); each warrants a separate invocation. Did not open `model.xlsx` per agent instructions. The R&D $34-vs-$36 inconsistency surfaced because the chart segment value diverges from the prose paragraph; flagged as NICE-TO-HAVE because it's an internal-consistency issue rather than a visual-design issue, but the writer may want to resolve it while editing the chart script.
