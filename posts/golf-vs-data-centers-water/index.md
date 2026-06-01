---
title: "Golf uses more water than data centers. By 2x, or by 100x, depending how you count."
description: "Golf out-waters US data centers by anywhere from 2x to 100x, depending on whether you count the electricity behind the servers and which year you stand in."
pubDate: 2026-05-30
tags: [water, data-centers, AI, golf, napkin-math]
---

My second son raised a claim that has been making the rounds in defense of the AI buildout: golf courses use far more water than data centers, so the outrage about server farms draining the reservoirs is misplaced. Both golf and AI are things a society could choose to do without, which makes them fair to weigh against each other in a way that comparing data centers to farms is not.

Using the back of a napkin, golf does use more water than data centers today, by somewhere between 2 times and 100 times. Which number you get depends on two choices: whether you count the water used to make the electricity, and your time horizon. Get to 2028 on the central assumptions and the comparison flips.

## Why not compare AI to farming?

US agriculture consumes something like 73 billion gallons of water a day through irrigation, per the USGS.[^1] That is roughly 27 trillion gallons a year. Golf and data centers together are a rounding error against it. So why not compare AI to farming?

Golf and AI are both discretionary. You can argue about how discretionary AI is, but nobody starves if a hyperscaler delays a training run, and nobody starves if a fairway goes brown.

Everything below is United States, national, and annual. The figures are consumption, not withdrawal: water that evaporates or transpires and never returns to the source, rather than water that is borrowed and largely given back. Holding both sides to consumption is the choice that moves the answer most.

## "A golf club uses more water than ChatGPT"

The viral form is blunt. "A single golf club uses more water than ChatGPT."[^2] Analyst write-ups and local-news explainers run the same play: golf in the United States uses on the order of 1.5 to 2 billion gallons a day, data centers use about 17 billion gallons a year, so golf wins by many multiples. One widely shared Arizona analysis put Maricopa County golf at roughly 30 times the water of the county's data centers and concluded the server farms are not the villains.[^3]

The figures these pieces cite are real. Golf's applied irrigation water for 2024 was 1.63 million acre-feet, per the GCSAA and USGA's environmental survey (the fourth round, published in 2025).[^4] Data centers' direct on-site water consumption for 2023 was about 17 billion gallons, per Lawrence Berkeley National Laboratory's December 2024 report.[^5] Side by side, golf is roughly 24 times larger.

But those two numbers are not apples to apples.

## Three ways the comparison goes wrong

In increasing order of impact:

### Golf's number is water borrowed; the data center number is water gone

Golf's 1.63 million acre-feet is *applied* water, the amount sprayed on the turf. A good chunk of that soaks back into the ground or runs off and returns to the source. The portion actually consumed, lost to evaporation and transpiration, is lower. How much lower is unknown. No survey measures it. The turf-irrigation literature supports something in the range of 70 to 90 percent consumed,[^6] so I modeled it as a low/central/high band and labeled it for what it is, an assumption rather than a measurement.

At the central 80 percent, golf's 1.63 million acre-feet of applied water (531 billion gallons) becomes about 425 billion gallons consumed. Across the 70-to-90 band, golf falls between 360 and 493 billion gallons. So this correction shaves golf down by a tenth to a third.

### The data center number leaves out the thirstiest part

The 17 billion gallons is only the water that evaporates inside the building, in the cooling towers. It ignores the water consumed at the power plants making the electricity the servers run on. LBNL puts that indirect figure at about 210 billion gallons for 2023, more than twelve times the on-site number.[^5] Counting it takes total data center water consumption to roughly 228 billion gallons.

That single addition closes most of the gap. Against data centers' direct water alone, golf consumes about 24 times more. Against the full footprint including the electricity, golf consumes about 1.9 times more. The gap goes from "not a contest" to "roughly double."

But that 210 billion gallons is a high estimate. LBNL uses a grid-average water intensity of 4.52 liters per kilowatt-hour,[^5] which includes evaporation off hydropower reservoirs and averages across the whole grid. New data center load does not draw on the average grid. It draws on new gas plants and renewables, which consume far less, closer to 0.8 liters per kilowatt-hour.[^7] Swap in that marginal figure and indirect water roughly quarters, the widest single variable in the model. The central case keeps LBNL's published number; flip to the marginal view and the gap to golf widens back out.

### The national number hides where the water actually is

Both uses are national aggregates. Golf is spread across roughly 14,000 facilities. Data center water clusters in a handful of metros, several of them already short on water.

Maricopa County, Arizona is the test case, because it is dense in both. Even there, golf wins on totals: Phoenix-area golf runs near 99,500 acre-feet a year[^8] against a few thousand acre-feet for the state's operating data centers,[^9] a gap of around 35 times. The national result survives at the county level.

It does not survive at the level of a single address. An average Phoenix golf course consumes about 504 acre-feet a year.[^8] Meta's Mesa campus, at full build-out, is planned for about 1,400 acre-feet.[^10] That is the water of nearly three golf courses, concentrated at one site and drawing from one local supply. Golf is more water spread thin. A hyperscale campus is less water concentrated to a point. If your worry is a regional aquifer, watch the campus drawing from it, not the national total.

## Golf leads now, but the gap is closing

Golf still uses more water than data centers today. That much holds up under every framing in the model. But "how much more" ranges across the four cells from about 1.9 times to about 106 times, and a fair version of the claim has to say which cell it is standing in.

| Data center framing | Water consumed, B gal/yr | Golf to data center |
|---|---|---|
| Direct only, all data centers | 17 | 24x |
| Direct only, AI's share | 4 | 106x |
| Direct + indirect, all data centers | 228 | 1.9x |
| Direct + indirect, AI's share | 52 | 8x |
| Golf (consumed) | 425 | reference |

The popular comparison lives in the top-left cell, golf against on-site data center water, where the ratio is largest. The most complete comparison, total footprint against total footprint, is the row where golf leads by less than two to one. If you narrow to the slice of data center water that is specifically AI rather than ordinary cloud computing, golf pulls ahead again, by roughly 8 times on the attributional method, more if you measure AI's share another way. AI's share is itself uncertain. It increasingly runs on the same shared infrastructure as everything else, so there is no clean line around it. The model offers three ways to draw the line and they disagree.

![Golf still uses more, but the framing decides whether it is 2x or 100x](assets/chart1_spread.png)

What does not survive is the idea that the comparison is stable. Golf's water is flat and slightly declining; the survey has it down 3 percent since 2020.[^4] Data center water is compounding at something like 20 percent a year as the buildout runs.[^5] So the gap is a moving target. On the central assumptions, total data center water consumption passes golf around 2026, about now, and reaches roughly 590 billion gallons by 2028 against golf's flat 425. What flips the comparison is not how you measure golf or how you define AI. It is time.

![Golf is flat. Data center water is not. In the central case they cross around 2026.](assets/chart2_flip.png)

The crossover rides on the indirect-water intensity, where the model is least sure of itself. Hold to LBNL's grid-average number and the lines cross before 2028. Use the marginal gas-and-renewables figure instead and golf keeps its lead past 2030. Both are defensible. The reasonable conclusion is not a date but a direction: a comparison that currently favors golf is being pushed toward parity every year, and the speed depends on how the grid that powers the servers gets built.

## Per gallon, the value runs the other way

Water is only one side of the ledger. The other is what the water buys, and there the comparison inverts. Golf's courses take in about $35.7 billion a year in direct revenue (IBISWorld),[^11] which against 425 billion gallons is roughly 8 cents per gallon consumed. US data centers earn around $208 billion (Arizton)[^12] on 228 billion gallons, about 92 cents a gallon, eleven times golf's water productivity. Golf wins the gallons fight by nearly two to one. On value per gallon it loses by far more.

Put it as a breakeven. To match golf's revenue per gallon, US data centers would need to produce about $19 billion a year. They produce more than ten times that. Even AI on its own, the contested slice, would need about $4.4 billion against its roughly 52 billion gallons, and S&P Global puts US generative-AI revenue near $13 billion.[^13] Two caveats: value per gallon rewards whatever is not water-hungry, and turf is the thirstiest dollar in this comparison. And revenue misses both the recreation a course provides and the productivity AI only promises. The broad economic-impact totals (golf at $102 billion,[^14] data centers at $727 billion)[^15] point the same way but lean on industry-commissioned multipliers, so the narrower revenue is the safer figure.

![Golf leads on water by 1.9 times; data centers lead on value per gallon by 11 times](assets/chart3_value_flip.png)

Neither side is the water villain. Against agriculture, both are trivial: golf's 425 billion gallons is about 1.6 percent of what US irrigation consumes.[^1] "Golf uses way more water than data centers" is true, but only inside a specific and increasingly dated framing.

*Every figure here comes from a [spreadsheet model](https://github.com/davidjk/napkinquest-articles-public/blob/main/posts/golf-vs-data-centers-water/model.xlsx). Change one assumption, the AI method, the projection year, the golf consumption fraction, or the electricity water intensity, and the four cells move with you.*

## Sources

[^1]: U.S. Geological Survey. "Estimated Use of Water in the United States in 2015." Fact Sheet 2018-3035 / Circular 1441, 2018. https://pubs.usgs.gov/fs/2018/3035/fs20183035.pdf — Irrigation consumptive use 73.2 billion gallons/day; the most recent complete national compilation.

[^2]: Warp News. "A single golf club uses more water than ChatGPT." https://www.warpnews.org/premium-content/a-single-golf-club-uses-more-water-than-chatgpt/

[^3]: Andy Masley analysis, reported by azfamily.com. "Data centers aren't the water villains you think they are, environmentalist says." February 26, 2026. https://www.azfamily.com/2026/02/26/data-centers-arent-water-villains-you-think-they-are-environmentalist-says/

[^4]: Shaddox, T.W., Unruh, J.B., Tapp, J., Brown, C.D., Stacey, G., Fuger, E. "Survey of Water Use and Management Practices on US Golf Courses from 2005 to 2024." *HortTechnology* 35(5):848-857, 2025. https://doi.org/10.21273/HORTTECH05716-25 — Fourth round of the GCSAA/USGA Golf Course Environmental Profile water survey. Applied (delivered-to-turf) water of 1.63 million acre-feet in 2024, down 3.2% vs 2020.

[^5]: Shehabi, A., et al. "2024 United States Data Center Energy Usage Report." Lawrence Berkeley National Laboratory, LBNL-2001637, December 2024. https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf — Direct on-site water 66 billion liters (17.4 billion gallons, 2023); indirect electricity-generation water ~800 billion liters (~211 billion gallons); grid-average water intensity 4.52 L/kWh; electricity 176 TWh (2023) rising to 325–580 TWh by 2028, the basis for the data-center growth trajectory.

[^6]: ET consumption fraction (70/80/90%) is a modeling assumption — no survey-grade national turf figure exists. Bracketed from irrigation-efficiency literature: NRCS Irrigation Toolbox, "Efficiencies"; University of Nebraska–Lincoln Extension G2191.

[^7]: Macknick, J., Newmark, R., Heath, G., Hallett, K.C. "Operational water consumption and withdrawal factors for electricity generating technologies." *Environmental Research Letters* 7, 045802, 2012. https://doi.org/10.1088/1748-9326/7/4/045802 — Natural-gas combined-cycle (recirculating) ~0.78 L/kWh; wind and solar PV ~0. Used to represent a marginal gas-and-renewables grid the new load actually draws on.

[^8]: Arizona Water Resources Research Center / Arizona Department of Water Resources. "Golf Course Water Use." https://wrrc.arizona.edu/sites/wrrc.arizona.edu/files/documents/SS-Golf-Course-Water-Use-4-19-23.pdf — Phoenix AMA golf ~99,500 acre-feet/year across ~174 courses; ~504 acre-feet average per course.

[^9]: Bluefield Research, via WaterDesk / Circle of Blue. "Data centers: a small but growing factor in Arizona's water budget." April 2025. https://waterdesk.org/2025/04/data-centers-a-small-but-growing-factor-in-arizonas-water-budget/ — Operating Arizona data centers ~905 million gallons (~2,777 acre-feet), under 0.1% of state water.

[^10]: Meta Mesa campus full build-out planned at ~1,400 acre-feet/year. DataCenterDynamics; Arizona Department of Water Resources.

[^11]: IBISWorld. "Golf Courses & Country Clubs in the US — Market Research Report." IBISWorld, 2026. https://www.ibisworld.com/united-states/industry/golf-courses-country-clubs/1652/ — US golf courses & country clubs industry revenue ~$35 billion (public summary ~$34.8–35.5B; the exact $35.7B edition is paywalled).

[^12]: Arizton Advisory & Intelligence. "United States Data Center Market — Industry Analysis, Market Size, Investments." Arizton, 2025. https://www.arizton.com/market-reports/us-data-center-market-analysis — US data center market valued at USD 208.38 billion (2024).

[^13]: S&P Global Market Intelligence (451 Research). "Generative AI market revenue projected to grow at a 40% CAGR from 2024–2029." 2024. https://www.spglobal.com/market-intelligence/en/news-insights/research/generative-ai-market-revenue-projected-to-grow-at-a-40-cagr-from-2024-2029 — S&P's public figures are global (~$16 billion total generative-AI revenue in 2024, North America–based providers ~63%, implying ~$10 billion). The "near $13 billion" US figure sits between that implied share and the global total; the breakeven of ~$4.4 billion clears at either number.

[^14]: National Golf Foundation, commissioned by the American Golf Industry Coalition. "Golf Economic Impact Report 2023." 2023. https://www.ngf.org/member-publication/golf-economic-impact-report-2023/ — Golf's direct US economic impact almost $102 billion; $226.5 billion total including indirect and induced effects.

[^15]: PwC, commissioned by the Data Center Coalition. "Economic Contributions of Data Centers in the United States, 2017–2023." 2025. https://www.centerofyourdigitalworld.org/2025-impact-study — US data center annual contribution to GDP grew from $355 billion (2017) to $727 billion (2023).
