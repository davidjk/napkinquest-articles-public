---
title: 'Can a Frontier AI Lab Pay Its Own Compute Bill?'
description: 'In May we priced a million tokens at $154. Anthropic''s S-1 lets us check the work, and ask what growth the labs'' compute commitments assume.'
pubDate: 2026-11-03
tags: ['ai', 'economics']
---

In May we asked [what it costs a frontier AI lab to serve a million tokens](https://napkinquest.com/posts/cost-of-a-million-tokens/), the unit these companies sell their models by. The answer we got was $154, and almost all of it was fixed cost: training runs, researchers, and above all the data centers. Fixed costs get cheaper per token as volume grows, so the question became one of demand. The labs' spending only made sense if the industry roughly doubled the tokens it served. If demand kept compounding, all three frontier labs (OpenAI, Anthropic and Google) would come out fine; if it stalled, one of them probably wouldn't.

Five months later we can check that work against real numbers. Anthropic has filed to go public, and its S-1, the registration statement a company files with the SEC before an IPO, is the first time one of these labs has opened its books. What it shows is better for the labs than our May model suggested: the leading lab now roughly covers all its costs, training included, from what customers pay it, and its contracts need much less growth than it's getting. The strain we were looking for is real, but on our rough numbers it has moved to the companies that build the data centers the labs rent.

## Was $154 a Million Tokens Right?

It was too high, mostly because we spread the fixed costs over too few tokens. The May model assumed the whole industry served about 250 trillion output tokens a year. The article itself cited OpenAI's roughly $2 billion of 2024 inference spending, and at the model's own cost per token that implies about 305 trillion for OpenAI alone. Fix just that and $154 becomes about $33 per million tokens.[^1] Even that is generous: Google alone now runs about 17 quadrillion tokens a year through its APIs.[^2]

We also had the prices wrong. We said frontier tokens sold for $15 to $75 per million, but on the day we published Anthropic's flagship listed at $25 per million output tokens, and the mid-tier models most developers use now cost $10 to $20.[^3]

And the "1.9x" demand figure, the doubling at the center of the May piece, turned out not to measure demand at all. Token volume cancels out of the formula; what's left is the labs' spending commitments divided by one lab's annual costs.

Some of the May article held up. OpenAI looked like the most exposed of the three labs, and it still does. Free users and heavy users on flat-rate plans looked like the place the losses concentrate, and they still are.[^23]

## Does a Lab Cover Its Costs Yet?

Anthropic roughly does now, training included. Serving customers is very profitable: in the first half of 2026 it cost $2.4 billion against $16.3 billion of revenue. But serving is the small part. Once you add training, research, salaries and sales, Anthropic lost $693 million on that revenue, an operating margin of about −4%, or a profit of about 10% on the company's adjusted measure, which leaves out stock compensation.[^4] A year earlier it lost $2.1 billion on $1.2 billion of revenue, and its cash from operations has since turned positive.

Anthropic's profit will look worse on paper after the IPO. Most of the stock it has granted employees only counts as an expense once the company goes public, and the S-1 says that will add about $23.7 billion of costs, mostly over the next two years.[^4] That's around $11 billion a year, about a sixth of current revenue, enough to put the company back into an operating loss. None of it is cash, so it doesn't change whether Anthropic can pay its compute bill, but it is a real cost to shareholders.

Most of that revenue, 80%, comes from customers paying per token, so falling token prices hit it directly. About half of all Anthropic's revenue reaches it through Amazon, Google and Microsoft, whose cloud customers can buy Anthropic's models through their existing cloud accounts. Those three companies are also Anthropic's investors and the suppliers of its compute, which makes the revenue look circular. The money in those sales still comes from the end customers who buy through those accounts.[^4]

OpenAI is further from covering its costs. It spends far more on research and training relative to its revenue: $19.2 billion of R&D in 2025 against $13.1 billion of revenue.[^22] Its free users add to the gap. Only about 6% of ChatGPT's weekly users pay,[^5] and in 2025 nearly half of OpenAI's $8.4 billion inference bill went to people who don't pay at all.[^6] In the first quarter of 2026, investors' money still covered about 40% of its cash spending, and in the second quarter it lost $12.3 billion on $6.7 billion of revenue.[^7]

The labs are responding by moving heavy users onto the meter. GitHub switched its Copilot coding assistant to token-based billing in June, Anthropic now charges business seats for every token used, and OpenAI has reportedly brought back usage caps on its $20 plan.[^8]

## What Growth Does Anthropic Need to Pay Its Compute Bill?

Anthropic needs its revenue to grow a little under 30% a year, far less than it's growing now.

Anthropic doesn't own most of its computers. It rents them from Google, Amazon, Microsoft and others under long contracts, and most of those contracts require it to pay whether or not it uses the capacity. Those firm commitments come to nearly $400 billion, or about $59 billion a year once they're all running.[^9]

With Anthropic's other costs, it needs about $111 billion of revenue in 2028 to cover everything. It earns about $67 billion a year now, so it needs a bit under 30% growth a year to get there.[^10] Its own plan, about $195 billion in 2028, takes about 70%.[^11]

It has signed up for another $200 billion of computing on top of that. Anthropic can cancel the largest piece, about $120 billion with SpaceXAI, on 90 days' notice. The rest, with Nscale and Lambda, it can't cancel but pays for only as the capacity is delivered; counting those as firm too raises the growth it needs to about 36% a year.[^9]

## What Could Go Wrong?

The price of a token could fall faster than the number of tokens grows.

Revenue is tokens sold times the price per token, and the price keeps falling. Ramp, a corporate-card company that tracks what businesses spend on AI, says the price businesses paid per token across the labs fell 41% between its March peak and early September.[^14] List prices for the models most developers use fell even faster, by 35% to 60% between May and October.[^12] Kept up for a year, Ramp's pace is about a 65% decline, and at that rate Anthropic needs to sell nearly 4 times as many tokens each year just to cover its commitments.

That's about as fast as token volume has been growing. Google's API tokens grew a little more than fourfold in the past year, and its tokens across all products grew 6.7 times in the year to May.[^2][^13] Those counts include free use, such as the AI answers in Google Search, so they overstate paid demand. Revenue is a better test: Anthropic's grew 45% from the second quarter to the third, a pace of more than four times a year. So far that's enough, but it leaves little room.

![Line chart of the token growth Anthropic needs each year to cover its compute commitments by 2028, against how fast the price per token falls. At the 65% annual price decline implied by Ramp's figures for what businesses paid, it needs 3.9x more tokens a year. A grey line for Anthropic's own 2028 plan runs above. Reference lines mark Google's API token growth (more than 4x in a year) and its token growth across all products, including free use (6.7x in the year to May).](./assets/breakeven.png)

So far volume has kept ahead. Anthropic's third-quarter revenue still rose 45% while that price fell. But three months is a short window, and there are early signs of slowing: Anthropic's third quarter was the first since at least early 2025 in which revenue grew by a smaller dollar amount than the quarter before.[^4][^10] Anthropic's compute spending, meanwhile, rises as its contracted capacity arrives, whether or not demand has. In the third quarter, compute spending grew about 77% over the second while revenue grew 45%, so the roughly break-even first half may not repeat as more committed capacity comes online.[^4][^10]

OpenAI faces a harder version of the same test. It needs revenue to grow about 68% a year just to cover its current costs by 2028, and about 90% a year to reach its own plan of $350 billion in 2030.[^15] Most of its revenue comes from flat-rate subscriptions, and growing those means signing up more paying users, which cheaper tokens don't do.[^16]

## How Is Google Doing on Both Sides?

Renting out capacity pays Google, but building it now costs more than the company earns. Google is both a frontier lab and one of the landlords the labs rent from, and the May article ended by asking whether selling its chips and data centers to a rival lab was smart or a slow erosion of its advantage. Its third-quarter results give a partial answer.

Google Cloud's revenue doubled to $30.7 billion in the third quarter, and its operating margin rose from 23.7% to 36.2% in a year.[^2] Anthropic is a big part of that: its commitment of at least $114.5 billion is about a fifth of Google Cloud's backlog of signed future business, and Google is also one of Anthropic's shareholders.[^4][^17]

Google's capital spending more than doubled from a year earlier, to $51.4 billion in the quarter, while cash from operations fell to $42.3 billion. That's the second quarter in a row it spent more than it brought in. To keep building, Google raised $29 billion of debt and sold $12.4 billion of new stock in the quarter, and it stopped buying back its own shares.[^2]

## So Where Is the Risk Now?

The risk is now with the companies building the data centers, which is where many critics have been looking all along. Michael Burry, the investor known from The Big Short, has argued that these companies write their chips off over too many years, which flatters their profits.[^18]

Amazon, Alphabet, Microsoft, Meta, Oracle and others are spending roughly $800 billion a year on AI data centers.[^19] For what's been built since 2023 to earn a normal return, customers would need to pay about $430 billion a year, or about $780 billion once the labs and products on top are counted. Our rough estimate is that they pay about $220 billion today.[^20]

Nobody pays that gap directly. The builders absorb it as a lower return on what they've built, and they borrow or issue stock to keep going. Oracle burned $5.4 billion of cash last quarter, and Google is now borrowing and issuing stock to keep up.[^21] If customer spending doesn't grow into all that capacity, the labs would feel it first, since their rent is fixed, and Anthropic's cash would cushion the blow for a while. If the shortfall lasted, much of the loss would reach the builders, who are also the labs' landlords, lenders and shareholders.

## What Would Change the Answer?

- Whether the price businesses pay per token keeps falling at Ramp's pace through the fourth quarter.
- Whether Anthropic's growth keeps slowing.
- Whether $125 billion to $150 billion of additional chips Anthropic expects from 2028 to 2031 arrives on schedule. At full run it would add $31 billion to $37 billion a year to the bill.[^4]
- Whether Anthropic's cash flow stays positive once it has used up compute it paid for in earlier years.

---

*For readers of the May piece, smaller fixes: Oracle's OpenAI backlog is about 66% of its total, not 54%; the R&D layer was $36 in the text and $34 in the chart; capex was 81% of the full economic cost, not 40%; the "two of three labs survive" finding was never modeled; and about three-quarters of Google's estimated cost advantage came from an assumption about its cost of capital that we never supported, with the TPU itself accounting for less than a tenth.*

*The model behind this analysis is available as a [spreadsheet with editable inputs](https://github.com/davidjk/napkinquest-articles-public/blob/main/posts/frontier-labs-reassessed/model.xlsx).*

---

## Sources

[^1]: The May figure on a full economic basis, $253, becomes about $49 with the same correction. Both restatements are in the model's "May vs Now" sheet.

[^2]: Alphabet Inc. "Alphabet Announces Third Quarter 2026 Results" and Q3 2026 earnings slides. October 28, 2026. https://abc.xyz/investor/. The 17 quadrillion is 32 billion tokens a minute annualized; most of those are input tokens, and it's two years after the May model's 2024 baseline, but even a small output share is far above 305 trillion.

[^3]: Anthropic, OpenAI and Google API pricing pages, as of May 15, 2026 and October 2026. https://claude.com/pricing; https://developers.openai.com/api/docs/pricing; https://ai.google.dev/pricing. On May 15 Anthropic's flagship listed at $25 per million output tokens, OpenAI's at $30 and Google's at $12.

[^4]: Anthropic PBC. Form S-1 Registration Statement. SEC, October 26, 2026. https://www.sec.gov/Archives/edgar/data/0002130357/000162828026067168/anthropicpbc-sx1.htm. The H1 2026 figures are unaudited. The $2.4 billion serving cost (an 85% gross margin) excludes compute for free users and the fees cloud marketplaces keep, both booked as sales and marketing. Adjusted operating income of $1.6 billion adds back $2.2 billion of stock compensation and a $126 million non-cash donation to the $693 million operating loss. Revenue is not directly comparable across labs: about 48% of revenue is sold through Amazon's, Google's and Microsoft's marketplaces and booked at the gross amount, while OpenAI's revenue is reported net of such partners. Operating cash flow of $3.9 billion was about $2.8 billion before working-capital swings, and close to break-even before adding back stock compensation. On completion of the offering, Anthropic expects to record $2.9 billion of cumulative stock compensation for restricted stock units and to recognize a further $23.7 billion over a weighted-average 2.1 years using accelerated attribution, so the early years carry more than the average; it also has $3.1 billion unrecognized for other awards. The $11 billion is the $23.7 billion spread over the S-1's weighted-average 2.1 years; accelerated attribution puts more in the early years. Against the second quarter's operating margin of about 8%, it implies an operating loss of roughly 8% of revenue; against the first half's, closer to 20%.

[^5]: TechCrunch. "ChatGPT reaches 900M weekly active users." February 27, 2026. https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users; with 50 million-plus paid subscribers per CNBC via Unite.AI (note 16).

[^6]: The Information, February 2026, via Safeguard. "OpenAI gross margin and inference spend: what has been reported." https://safeguard.sh/resources/blog/openai-gross-margin-and-inference-spend-what-has-been-reported

[^7]: The Information. "OpenAI burned $3.7 billion in first three months of 2026." June 16, 2026. https://www.theinformation.com/articles/openai-burned-3-7-billion-first-three-months-2026; Investing.com. "OpenAI's Q2 revenue growth lagged Anthropic as losses deepened, WSJ reports." August 19, 2026. https://uk.investing.com/news/stock-market-news/openais-q2-revenue-growth-lagged-anthropic-as-losses-deepened-wsj-reports-4837981

[^8]: GitHub. "GitHub Copilot is moving to usage-based billing." 2026. https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/; The Register. "Anthropic ejects bundled tokens from enterprise seat deal." April 16, 2026. https://www.theregister.com/software/2026/04/16/anthropic-ejects-bundled-tokens-from-enterprise-seat-deal/5226555; Admix. "ChatGPT Plus 5-hour limit returns." August 2026. https://admix.software/blog/chatgpt-plus-5-hour-limit-returns

[^9]: Anthropic S-1 (note 4). The firm commitments are Google ($114.5 billion through mid-2033), Amazon ($110.0 billion through 2036), Microsoft ($44.9 billion through 2033) and a five-year Broadcom chip lease ($125.2 billion). The yearly figure spreads each evenly over its term; the S-1 doesn't give a year-by-year schedule. Google and Amazon are owed true-ups if Anthropic's spending falls short, "subject to certain adjustments and exceptions," and Google, Amazon and Microsoft are also Anthropic shareholders. The remaining agreements, with SpaceXAI (cancelable on 90 days' notice from early 2027), Nscale and Lambda (non-cancelable apart from supplier failures, paid as delivered), total about $206 billion; if all of it arrived by 2028, the growth needed would be closer to 57% a year. A non-cancelable AMD commitment from 2027, which the S-1 expects to exceed $20 billion but gives no fixed amount for, is outside all of these figures. Covering the commitments also assumes Anthropic keeps making its models cheaper to run on the chips it has committed to.

[^10]: CNBC. "Anthropic's third-quarter revenue hits $16.8 billion." October 15, 2026. https://www.cnbc.com/2026/10/15/anthropics-third-quarter-revenue-hits-16point8-billion-ipo.html. CNBC reports $1.70 of revenue per dollar of compute in the third quarter, implying about $9.9 billion of compute. Anthropic buys compute 12 to 18 months ahead, and the S-1 says its compute expense rises as contracted capacity becomes available rather than with in-period demand; the S-1's quarterly table shows $5.6 billion of compute and $11.6 billion of revenue in the second quarter.

[^11]: Reuters, via Investing.com. "Anthropic IPO valuation hinges on $190-200 billion 2028 revenue forecast, sources say." August 17, 2026. https://www.investing.com/news/stock-market-news/anthropic-ipo-valuation-hinges-on-190200-billion-2028-revenue-forecast-sources-say-4862222

[^12]: Anthropic, OpenAI and Google pricing pages (note 3), May to October 2026: the default models most developers call went from $20 to $30 per million output tokens to $10 to $20. Some flagship and introductory prices rose over the same period. The token multiples also allow for about 5% of volume a year moving to cheaper open-weight models.

[^13]: Pichai, Sundar. Google I/O 2026 keynote remarks (3.2 quadrillion tokens a month, up from 480 trillion a year earlier). May 19, 2026. https://blog.google/innovation-and-ai/sundar-pichai-io-2026/

[^14]: Ramp. "AI Index, September 2026." https://ramp.com/data/ai-index-sept-2026. The effective price per million tokens fell from $1.15 in March to $0.68 in early September, across the labs Ramp tracks; the annual figure compounds that six-month change. The weekly series is noisy: Ramp's October index has Anthropic at $0.61 in the week ending October 23, down 16% in one week (https://ramp.com/data/ai-index). It's based on corporate-card spending, which misses sales through cloud marketplaces and contracted enterprise deals. Some of the drop is customers moving to cheaper models or to cached tokens, which cost less to sell and to serve. Chinese models, nearly all open-weight, carried 57% to 67% of tokens on OpenRouter, a developer marketplace, in mid-September (CNBC, September 26, 2026, https://www.cnbc.com/2026/09/26/china-ai-global-adoption.html).

[^15]: The Next Web. "OpenAI's $856bn compute plan vs $600bn reset." September 2026. https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved

[^16]: Unite.AI, citing CNBC. "OpenAI tells investors enterprise revenue has overtaken its ChatGPT consumer business." August 2026. https://www.unite.ai/openai-tells-investors-enterprise-revenue-has-overtaken-its-chatgpt-consumer-business/. About half of OpenAI's revenue comes from consumers, and much of the rest from per-seat business subscriptions. OpenAI reported 50 million-plus paid subscribers in March.

[^17]: Alphabet Inc. Form 10-Q for the quarter ended September 30, 2026. https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm. Cloud backlog was $560.8 billion. On the lab side, Google serves about 32 billion tokens a minute through its APIs and the Gemini app has a billion monthly users; Google doesn't say what Gemini earns. Part of Cloud's growth is one-time sales of TPU systems, Google's own AI chips, which the release doesn't split from recurring cloud revenue.

[^18]: Fortune. "The Big Short investor's AI bubble case, explained." November 13, 2025. https://fortune.com/2025/11/13/the-big-short-investor-closing-scion-ai-bubble-depreciation-explained

[^19]: Goldman Sachs hyperscaler capex estimates, via Advisor Analyst. "AI capex, required revenues, and what the market is actually pricing." October 15, 2026. https://advisoranalyst.com/2026/10/15/ai-capex-required-revenues-and-what-the-market-is-actually-pricing.html/

[^20]: Model "System" sheet. The roughly $1.4 trillion built since 2023 is written off over five years for chips and twenty for buildings at a 9% cost of capital. The $780 billion applies Anthropic's ratio of compute to revenue. The $220 billion is our estimate, within a range of $190 billion to $255 billion, mostly lab subscriptions and API fees, cloud AI services and Copilot-style add-ons. It's the least certain number here: much of Meta's and Google's spending serves their own ads and Search, where the return shows up as ad revenue nobody counts as AI, and longer chip lives would shrink the requirement.

[^21]: Oracle. Q1 FY27 earnings slides. September 2026. https://s23.q4cdn.com/440135859/files/content_files/Q1-FY27-Oracle-Earnings-Slides.pdf; Alphabet (note 2).

[^22]: OpenAI's 2025 financial statements, as reported by the Financial Times and relayed by Yahoo Finance. "OpenAI 2025 financials leaked." June 2026. https://finance.yahoo.com/markets/stocks/articles/openai-2025-financials-leaked-38-121508294.html

[^23]: SemiAnalysis. "Anthropic subscriptions offer 5x." October 5, 2026. https://newsletter.semianalysis.com/p/anthropic-subscriptions-offer-5x. SemiAnalysis estimates subscriptions bring in about 10% of Anthropic's revenue but can use more than 40% of its inference compute, and that a subscriber using a top model at full capacity loses money several times over; the S-1 calls subscriptions "structurally more compute-intensive." Light subscribers are profitable: the model puts Anthropic's overall subscription gross margin near 70%.
