# Review: What does a million tokens cost a frontier AI lab?

**Draft:** ./index.md
**Generated:** 2026-05-10T00:00:00Z

This file is the writer's interface for the review. Mark each punch-list item with one of `[x]` accept · `[~]` modify · `[ ]` skip. For `[~]`, add an indented `**Modify:** ...` line describing the change. For inventory items, change the `**Disposition:**` keyword to one of `cut` / `strengthen` / `hedge` / `keep`. Untouched items stay as-is (skip for punch list, keep for inventory). When done, say "process the review."

## Punch list

- [~] **1. [CRITICAL] Colossus 1 GPU mix overstates what the source supports**

  **Where:** line 74: "300 megawatts of capacity and over 220,000 Nvidia GPUs spanning H100, H200, and GB200 accelerators, available within the month."
  **Issue:** Anthropic's own announcement (the cited [^8] source) gives only aggregates ("over 220,000 NVIDIA GPUs" and "more than 300 megawatts"). It does not break the fleet down by accelerator type. Public reporting (Tom's Hardware) describes the mix as "predominantly H100" plus "about 30,000 newer Blackwell units" — i.e. H100 + GB200. H200 is not corroborated by Anthropic or by major secondary reporting. Stating three specific accelerators implies a granularity the source doesn't grant.
  **Suggested fix:** drop the GPU list to what's sourced ("over 220,000 Nvidia GPUs"), or hedge to "predominantly H100 with newer Blackwell capacity, per public reporting." If you have a separate source that confirms H200, cite it.
  **Modify:** Drop the three-accelerator list. Use: "300 megawatts of capacity and over 220,000 Nvidia GPUs, predominantly H100 with newer Blackwell capacity per public reporting, available within the month."

- [x] **2. [IMPORTANT] "Not 10% lower. Roughly thirty percent lower" violates V3**

  **Where:** line 60: "Stack these and the model puts Google's cost per token around 70% to 75% of the standalone-lab baseline, on either basis. Not 10% lower. Roughly thirty percent lower, across every relevant layer."
  **Issue:** The "Not X. Y." pattern is textbook V3 corrective phrasing — it tells the reader they were imagining the wrong magnitude and corrects them. The 70-75% already delivers the finding cleanly; the "not 10% lower" sentence is editorial commentary that adds preaching to a number that doesn't need it.
  **Suggested fix:** cut "Not 10% lower." Either keep "Roughly thirty percent lower, across every relevant layer." as emphasis, or cut both sentences and let the 70-75% figure stand alone.

- [~] **3. [IMPORTANT] "Can the doubling actually happen?" header — V3 and V11**

  **Where:** line 98 (section header)
  **Issue:** "actually" in a header is a corrective tell (V3), and the question maps directly to the immediately-preceding section's framing without adding information (V11 says headers should carry a finding or sharper question, not a topic restatement). The body of this section reports two pieces of evidence: Anthropic's $30B run rate (bull) and overbuild + Broadcom counterparty risk + supply-side fragility (bear). The header could carry one of those findings.
  **Suggested fix:** something like "## $30 billion run rate, with three caveats" or "## The run rate looks healthy. The supply side doesn't." or just "## Is the doubling on track?" (drops the "actually").
  **Modify:** Use "## The run rate looks healthy. The supply side doesn't." — carries both halves of the section's findings.

- [~] **4. [IMPORTANT] "A fork, not a hedge" — V3 corrective**

  **Where:** line 124: "The two-scenario answer is a fork, not a hedge: both scenarios look reasonable from where the data sits in May 2026."
  **Issue:** "X, not Y" pattern (V3). Anticipates the reader thinking "two scenarios sounds like a cop-out" and corrects them. If the worry is real, address it in the prose ("both branches assert specific conditions the reader can check"); don't preempt and rebut.
  **Suggested fix:** "Both scenarios look reasonable from where the data sits in May 2026, each on specific conditions you can check against the diagnostic ratios above." Or just cut "is a fork, not a hedge:" and let the rest of the sentence carry the work.
  **Modify:** Cut "is a fork, not a hedge:" — change sentence to: "Both scenarios look reasonable from where the data sits in May 2026, each on conditions the diagnostic ratios above can check."

- [x] **5. [IMPORTANT] Closing italic note retroactively softens the whole piece (V9)**

  **Where:** line 132: "*The model behind this analysis is available as a [spreadsheet with editable inputs](#). All assumptions can be flexed; the numbers reported here come from midpoint scenarios that reflect the author's best triangulated estimates. The framework is the contribution; the specific dollar figures are illustrative.*"
  **Issue:** "The framework is the contribution; the specific dollar figures are illustrative" is V9 throat-clearing in the closing position. After a piece that defended specific numbers ($154, $253, $103, 1.9x, 158T, 19.8M, etc.), telling the reader those numbers are "illustrative" reads as the writer pre-disclaiming the work. The hedge at line 16 ("I'd update most of these conclusions if the key inputs turned out to be off by a lot") already does this job once, lightly.
  **Suggested fix:** cut the second and third sentences of the italic note. Keep the link to the spreadsheet; drop the meta-framing.

- [~] **6. [IMPORTANT] "$300 billion-plus search and ads business" is overstated for 2024**

  **Where:** line 58 and line 116: "self-funds AI investment from a $300 billion-plus search and ads business" / "self-funded from a $300 billion search and ads business"
  **Issue:** Alphabet's total 2024 ad revenue was $264B (Statista; Google Search & Other alone was $198B). Total Alphabet revenue was $350B but that includes Cloud, hardware, and Other Bets. "$300 billion-plus search and ads" is too high for 2024 actuals — it conflates total Alphabet revenue with ads. By 2026 the figure may be in range, but neither line clarifies the year.
  **Suggested fix:** "$260 billion-plus ad business" for 2024, or "$300 billion-plus revenue base" if you want to include Cloud, or qualify by year.
  **Modify:** Replace both instances with "$260 billion-plus ad business" (line 58 + line 116) to match 2024 actuals.

- [~] **7. [IMPORTANT] "Enterprise gross margins are 70%-plus" is unsourced**

  **Where:** line 121: "Heavy consumer users go negative at full-economic cost; enterprise gross margins are 70%-plus."
  **Issue:** This is asserted as fact in the diagnostic ratios. It's not in the verify register and there's no citation. The model has API pricing at $15-75 per million output tokens vs full-economic cost of $253 — at $75 against $253 the gross margin is *negative*, at $75 against $154 lab cash it's about 51%. The 70% figure needs either a citation, a definition of which enterprise tier, or to be derived from the spreadsheet explicitly.
  **Suggested fix:** either pull the number from the model's unit economics tab and cite the cell, or replace with the per-query margin range your model actually supports ("enterprise pricing at $50-75/M leaves room for margin against lab cash cost; full economic erodes it"). If the 70% claim depends on a specific assumption about input/output mix, name it.
  **Modify:** Replace with the margin range the model supports: "Heavy consumer users go negative at full-economic cost; enterprise pricing at $50 to $75 per million tokens leaves real gross margin against lab cash cost, though full economic erodes it. The higher the enterprise share, the more durable the business is to a demand stall."

- [~] **8. [IMPORTANT] Missing bull-case mechanism: agents and code, not consumer seats**

  **Where:** line 94: "Whether that's plausible depends on what 474 trillion tokens looks like in users. At today's heavy-user intensity ... the industry would need around 19.8 million heavy users. At the consumer median ... it's roughly 40 million paying seats at heavy-use-equivalent intensity."
  **Issue:** The plausibility check is anchored entirely on consumer-seat equivalents, but the strongest bull case for the doubling isn't 40M paying users — it's per-seat token intensity rising via agentic workloads, Claude Code, and inference-heavy enterprise pipelines. The article briefly nods to Claude Code (line 74) without connecting it to the demand math. A reader who's seen Cursor or Claude Code knows one developer can burn millions of tokens a day; that's the channel where doubling is plausible without seat growth.
  **Suggested fix:** add a sentence to the plausibility section noting that the seats math is conservative because per-user intensity is rising fast (agents, code, multi-step inference). Acknowledge that this strengthens the bull case the article otherwise treats symmetrically with the bear case.
  **Modify:** Add to the plausibility paragraph (after "Neither is implausible at current growth rates."): "And the seats math is conservative on its own terms. Per-user token intensity is rising fast — one developer using Claude Code or Cursor can burn millions of tokens a day, an order of magnitude above the consumer power-user assumption. Agentic workloads and inference-heavy enterprise pipelines push in the same direction. The doubling can happen without seat growth tracking it linearly."

- [~] **9. [IMPORTANT] OpenAI 2024 numbers are projection-stale**

  **Where:** line 8: "OpenAI lost $5 billion in 2024 on $3.7 billion in revenue,[^1]"
  **Issue:** Citation [^1] is a September 2024 CNBC piece reporting projected figures. OpenAI's actual 2024 revenue per later disclosures (CFO Sarah Friar, The Information) is reported variously at $4B+ (and possibly $6B per one CFO statement). The $5B loss figure may also be revised. Using projection-era numbers as if they were final actuals weakens the opening anchor.
  **Suggested fix:** update to the most recent reported figures with a current citation, or hedge the prose to "projected $5 billion loss on $3.7 billion in revenue (Sept 2024 reporting)" so the reader knows it's a snapshot. Either remove the strong "lost" verb if the number is a forecast, or anchor to the firmer $44B-through-2028 figure that's better-sourced.
  **Modify:** Hedge the prose. Change opening clause to: "OpenAI projected a $5 billion loss for 2024 on $3.7 billion in revenue per September 2024 reporting,[^1]" — preserves the anchor while signaling it's a snapshot.

- [ ] **10. [IMPORTANT] [^2] citation is a weak aggregator**

  **Where:** line 8, footnote 2: "TapTwice Digital. 8 OpenAI Statistics (2025): Revenue, Valuation, Profit, Funding."
  **Issue:** The $44B cumulative-loss projection is real and well-sourced, but the article cites a stats-aggregator blog rather than the source it's aggregating (The Information / OpenAI investor briefings, as reported by Yahoo Finance, Dataconomy, TMTPost). Engaged readers will check the citation; a TapTwice link doesn't survive that check.
  **Suggested fix:** swap [^2] for a primary or near-primary source (Dataconomy or TMTPost reporting The Information directly; or Sam Altman investor briefing coverage).

- [~] **11. [IMPORTANT] Section "Five layers of cost" header is a topic label (V11)**

  **Where:** line 18: "## Five layers of cost"
  **Issue:** V11 specifically calls out topic-label headers and prefers numbers/findings. "Five layers" is descriptive but not informational — the reader doesn't yet know which layer dominates. The voice.md gives "Capex is two-thirds of the cost stack" as the kind of header this should be.
  **Suggested fix:** something like "## Capex is the layer most analyses miss" or "## The cost stack: five layers, one dominates." This is the central finding of the section; the header should carry it.
  **Modify:** Replace with "## The cost stack: five layers, one dominates." — keeps the structural framing while carrying the finding.

- [~] **12. [NICE-TO-HAVE] "the one most analyses miss" — V3-adjacent**

  **Where:** line 30: "The fifth, and the one most analyses miss, is **capex amortization**."
  **Issue:** Mild V3 — "the one most analyses miss" positions the writer as catching what others got wrong. Voice.md prefers descriptive phrasings that let the reader draw the comparison.
  **Suggested fix:** "The fifth and largest is **capex amortization**." The size finding (largest layer) is the substantive surprise; the "most analyses miss" framing is editorial.
  **Modify:** Replace "The fifth, and the one most analyses miss, is **capex amortization**." with "The fifth and largest is **capex amortization**."

- [x] **13. [NICE-TO-HAVE] "actually" used three times as filler**

  **Where:** line 32 ("Lab cash is what the labs actually spend"), line 50 ("nobody can actually run that strategy unilaterally"), line 98 (header, already in #3).
  **Issue:** V3 flags "actually" as corrective. Two body uses plus a header is a stack. Each individually small; together they pattern as posture.
  **Suggested fix:** lines 32 and 50 read cleaner without "actually." "Lab cash is what the labs spend out of pocket" / "Nobody can run that strategy unilaterally."

- [x] **14. [NICE-TO-HAVE] "Investors are subsidizing... a real and growing business underneath" — slightly preachy**

  **Where:** line 40: "Investors are subsidizing the consumer flat rate and the next training run. Enterprise contracts and API usage, paying premium rates, are quietly funding a real and growing business underneath."
  **Issue:** "Quietly funding a real and growing business" is editorial flourish, not a number. V4 prefers findings as discoveries; this sentence asserts a verdict. Also "quietly" doesn't earn its place.
  **Suggested fix:** "Investors are subsidizing the consumer flat rate and the next training run. Enterprise and API usage, paying premium rates, fund the unsubsidized business underneath."

- [x] **15. [NICE-TO-HAVE] "fundamental tension" — M4 / M5 borderline**

  **Where:** line 42: "The flat-rate subscription model has a fundamental tension with heavy users that becomes more visible as costs are properly accounted for."
  **Issue:** "fundamental tension" is the kind of phrase that adds gravitas without adding precision. "Properly accounted for" is also editorializing (implies prior accounting was improper). Voice asks for plainness.
  **Suggested fix:** "Flat-rate pricing breaks down at heavy use. Usage caps and tiers are what that looks like in product."

- [ ] **16. [NICE-TO-HAVE] No chart**

  **Where:** N/A (absence)
  **Issue:** The default article structure prefers "one or two `nq chart` PNGs that make the central finding visible." This piece has at least two charts begging to exist: (a) the five-layer cost stack at lab-cash vs full-economic basis, side by side, and (b) the demand-implied tokens funnel from $200B commitment to 158T tokens to 19.8M heavy users / 40M seats. Both would speed up reader comprehension and validate the numbers visually.
  **Suggested fix:** generate the cost-stack bar chart via `nq chart`. Optionally a second showing the demand math.

- [x] **17. [NICE-TO-HAVE] Lede sentence 4 reads as methodology preview**

  **Where:** line 12: "Two cost figures fall out of the model and they answer different questions."
  **Issue:** V1 says lead with the question, not the methodology. This sentence frames the next paragraph as model output rather than answer. Could be tightened.
  **Suggested fix:** "Two cost figures answer different questions." (drop the methodology hop.) Or restructure so the $154 / $253 split is announced as the answer to "what does it cost," not as model output.

- [~] **18. [NICE-TO-HAVE] "Whether this proves wise depends on how those tradeoffs settle" — V9 anticipatory hedge**

  **Where:** line 82
  **Issue:** Promises an answer ("depends on how those tradeoffs settle") without delivering one. Reader is left with no specific conditions to check. Either commit or cut.
  **Suggested fix:** name the condition. "Whether this proves wise depends on whether TPU cloud revenue exceeds the discount Anthropic captures on its own training stack — which the model can't tell you, but the next two earnings cycles will."
  **Modify:** Cut the sentence "Whether this proves wise depends on how those tradeoffs settle." entirely. The prior sentence about dilution-for-revenue tradeoffs stands on its own.

- [~] **19. [NICE-TO-HAVE] "But not eliminated." sentence fragment after a transition**

  **Where:** line 102 (opens the paragraph)
  **Issue:** The fragment reads punchy in isolation but lands oddly because line 100 ended with "The bear case has weakened." Reading them together: "The bear case has weakened. But not eliminated." — the fragment is fine prose-wise but reads more like a tagline than analysis. Voice generally prefers asserting the next claim directly.
  **Suggested fix:** "The bear case has weakened. Three things keep it alive." Then list overbuild, Broadcom 8-K language, supply-side. Frame the section around the count.
  **Modify:** Replace "But not eliminated." with "Three things keep it alive." — the section already presents three (overbuild, Broadcom counterparty risk, supply-side), so the count carries.

## Inventory (writer to decide)

### Speculation — guesses about future or unobserved

- "If three labs each spend $5 billion to $10 billion annually on R&D and capex and the pool clears two of them, one folds, gets acquired, or settles into frontier-trailing status." (line 46) — predicting consolidation outcome conditional on demand stall. Not in the model.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "The first frontier lab to stop investing watches competitors capture its enterprise contracts within a year or two." (line 50) — speculation about competitive dynamics if a lab harvest-modes. Not modeled.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Strip out the investment and the business is gone in five years." (line 50) — speculation about lab obsolescence pace.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Whether this proves wise depends on how those tradeoffs settle." (line 82) — speculation deferring to future events; see punch-list #18.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Anthropic now closer to Google margin via TPU access" / "OpenAI now most disadvantaged" framing across the post-deal section — speculation about competitive position changes the model implies but the market hasn't priced.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

### Opinion / value judgment

- "Bulls and bears are arguing about which scenario, not whether the math could ever work." (line 14) — framing the public debate; substantive but interpretive.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Investors are subsidizing the consumer flat rate and the next training run." (line 40) — characterization of capital flows; see punch-list #14.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Enterprise contracts and API usage, paying premium rates, are quietly funding a real and growing business underneath." (line 40) — value-laden ("real," "quietly").
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "The flat-rate subscription model has a fundamental tension with heavy users that becomes more visible as costs are properly accounted for." (line 42) — "properly accounted for" implies prior accounting was improper.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "That's unusual disclosure language. Even suppliers think these commitments are fragile." (line 104) — interpretation of SEC filing language as signal.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "The two-scenario answer is a fork, not a hedge" (line 124) — defensive framing; see punch-list #4.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "For frontier labs as a category, the model leaves me thinking sustainable, with meaningful turbulence on the way." (line 124) — judgment.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

### Prediction / forecast

- "Inference cost decline rate ... 4x to 10x per year. The 1.9x demand multiple pencils out at the high end of that range and stops at the low end." (line 122) — forecast that the math works conditional on inference-cost trajectory.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "If revenue outpaces training spend, the model converges; if training spend outpaces revenue, it diverges." (line 120) — conditional forecast.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Neither is implausible at current growth rates." (line 94) — judgment about reachability of 19.8M heavy users / 40M seats.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Both numbers are well above today's consumer-paid base." (line 94) — assertion of fact disguised as judgment; could be sourced or pulled to a specific multiplier.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "If gigawatts pledged on paper cannot be delivered on schedule, the demand-side question ... and the supply-side question ... compound each other." (line 106) — conditional forecast.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

### Anecdote / personal experience used as evidence

- "I'd assumed the GPU bill would dominate before running the numbers; it doesn't." (line 24) — discovery anecdote supporting the inference-is-small finding. V2-clean use of first person.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "What surprised me when I re-ran the post-deal numbers was OpenAI's cell. It's the one that barely shifted." (line 84) — discovery anecdote supporting the OpenAI-most-exposed finding. V2-clean.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "Three diagnostic ratios are what I'd watch for which scenario plays out" (line 118) — first-person framing of the watchlist; defensible.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

- "For Google, I genuinely don't know whether monetizing the cost advantage will prove smart..." (line 126) — uncertainty disclosure. V2-clean.
  **Disposition:** _keep_  <!-- cut · strengthen · hedge · keep -->

---

**Findings:** 1 CRITICAL, 10 IMPORTANT, 8 NICE-TO-HAVE
**Inventory:** 5 speculation, 7 opinion, 5 prediction, 4 anecdote
**Top 3 issues to address before publishing:** 1, 7, 8
**Process notes:**
- Spreadsheet at `./model.xlsx`; verify.py registry confirms 18 cells + 9 prose patterns. Re-derived non-registered claims manually: Anthropic post-deal $138 lab cash (article says $137, within $1), pre-deal $155 (article $153), Google 74% of baseline (article 70-75%), Anthropic gap to Google 25pp → 15pp (matches), 11% cost drop (matches), consumer subsidy median $3 cash / $18 full-econ (matches), break-even ~216 cash / ~132 full-econ (matches), harvest 93% margin (matches). Numerical claims are clean.
- Web-verified: Google $40B Anthropic deal ✓, $350B valuation ✓, 5GW TPU ✓, $200B Google Cloud commitment ✓, Amazon $25B + 5GW Trainium ✓, $2T cloud backlog with Anthropic+OpenAI ~half ✓, Broadcom 8-K 3.5GW + counterparty language ✓, Anthropic $30B run rate from ~$9B end-2025 ✓, Dario 80x Q1 ✓, OpenAI Google TPU mid-2025 inference-only ✓, OpenAI $44B losses through 2028, profit 2029 ✓.
- Web-disputed: Colossus 1 GPU mix H100/H200/GB200 (only H100 + Blackwell corroborated; see #1). OpenAI 2024 actuals (cited number is Sept 2024 projection; later actuals diverge; see #9). Google "$300B search and ads" overstates 2024 ad revenue ($264B); see #6.
- No charts in `assets/`; flagged as NICE-TO-HAVE (#16).
- No steps skipped.
