---
name: market-opportunity-research
description: Evaluate business ideas and market opportunities through buyer demand, competitors, business models, and a first-customer validation plan. Use for commercial viability, competitor landscapes, founder journeys, or choosing between product, service, and partnership routes; not routine product shopping or technical implementation.
license: MIT
---

# Market Opportunity Research

## Purpose

Produce a decision-useful market investigation, not a generic industry overview or an ungrounded sales pitch. Help the user **understand the market, meet its real players, compare options, and decide what to test next**. Make a complex commercial question legible gradually. Preserve the user's goal, constraints, and current stage. Do not assume they should build a product.

The backbone is:

**Question → buyer & job → demand evidence → ecosystem & alternatives → commercial options → tradeoffs → falsifiable experiment.**

## When to use

- User has an idea, prototype, domain experience, or emerging technology and asks whether/how it could be a business.
- User requests competitor research, comparable founders/products, market mapping, customer demand, monetisation, first paid customers, or "who would buy this?".
- User is deciding whether to build software, offer a service, integrate with another vendor, or pursue a narrower niche.

Do **not** trigger for routine product shopping, general academic explanations, or technical implementation with no market decision. For a narrowly scoped sub-question, use only the relevant stages, not the entire report.

## Procedure

### 0. Frame the decision, not the technology

Restate in 1–3 sentences: what the user has, what they hope to achieve, whose decision this research should improve. Separate (a) what is established, (b) the user's hypotheses, and (c) important unknowns. Use current context. Ask only when a truly essential parameter is missing; otherwise state reasonable assumptions and proceed.

If the user says "train AI" or other broad terms, separate possible underlying jobs (knowledge access, memory, workflows, fine-tuning, embedding, analytics) before evaluating supply.

### 1. Unpack the buyer and the job-to-be-done

Identify who suffers, what their trigger/event is, what they do today, the cost of the present workaround, who uses vs who pays, and what result would count as valuable. Show buyer segments with grounded reasons and distinct workflows. Avoid assuming every organisation in a sector needs the product.

### 2. Verify that demand exists

Use available web/research tools for dated, attributable evidence. Look for behavioural or payment signals: existing contracts, customer deployments, case studies, market/usage data, review complaints, budgets, procurement, hiring and recurring manual work. Record geography, study date and sample; do not mix incompatible surveys. Label **adoption**, **interest**, **willingness to pay** and **actual payment** as different strengths of evidence.

See [references/evidence-standards.md](references/evidence-standards.md).

### 3. Map *real players*, not merely product names

Include the relevant ecosystem layers, selecting only those relevant to the topic:

- Direct products solving the same buyer job.
- Adjacent and enabling platforms/infrastructure.
- Service providers, integrators or consulting alternatives.
- In-house/manual substitutes or "do nothing".

For each significant player, explain target buyer, product/job, business model or pricing (when verified), evidence of customers, differentiation and constraints. Provide working primary links. For a full investigation, include **named, documented customer or founder journeys** when relevant and available; note if the evidence is self-reported. A list of logos alone does not satisfy this step.

### 4. Reframe the competitive question

Explain where the market is commoditised vs underserved, and distinguish **verified gap** from **possible gap**. Ask why customers would not simply buy from an existing player, use general AI, do it manually, or build in-house. Avoid claiming a moat because the technology works.

### 5. Offer meaningful strategic options and tradeoffs

Compare 2–4 genuinely different commercial routes when the scope warrants it (e.g. service-first, niche product-first, integration partner, infrastructure/SDK). Use buyer, time to first revenue, setup and support load, differentiation, distribution, margins, deployment/privacy burden and risks. Do not invent a numerical score to create precision. Give a conditional recommendation tied to the user's stage and constraints, plus what evidence would change it.

### 6. How money might change hands

Identify payer, unit of value, pricing models, one-time vs recurring revenue, implementation costs and support/hosting costs. Use sourced public price anchors *only as anchors*. Any proposed price not backed by transactions must be labelled **pricing hypothesis**. Do not treat consulting-directory budget bands as realised contracts. Offer an illustrative bottom-up value or unit-economics calculation only when inputs are explicit; separate time saved, capacity gained, realised cost saving and revenue.

### 7. Design a minimum paid learning experiment

Propose outreach, interviews, and pilots as a plan. Conducting outreach, contacting people, or committing funds requires the user’s authorization for that action.

Make the next action feasible for an individual or small team. Specify target customer profile, outreach and interview count as planning targets (not forecasts), what problems to observe, smallest bounded demonstration/pilot, metrics, decision-maker, requested payment or commitment, success criteria, kill/stop criteria and next iteration. Prefer payment or clear buying behaviour over "people liked the demo".

### 8. Write for progressive comprehension

For a full investigation, adapt [references/report-template.md](references/report-template.md); for a narrow question, answer only the relevant parts. Lead with a grounded thesis and 1–2 key distinctions, then move from evidence to names/examples, then options and implications, then execution. Explain jargon where it appears. Use compact tables for real comparisons, not a wall of bullet points. Place links adjacent to figures and named case studies.

The answer must feel like a **reasoned walkthrough**, not separate pasted research fragments. Respect the user's requested depth: a fast scan may be short, while deep research should substantiate founder/company histories with chronology and sources.

## Evidence discipline

- Verify changing information fresh when tools allow: prices, product status, roles, funding, customer logos, latest surveys. Include as-of dates and geographic/sample limits.
- Cite every external factual claim where supported. Prefer direct vendor pricing pages, company case studies, first-hand interviews, regulatory filings, reputable surveys, research and documented user accounts. Distinguish promotional case studies from independent verification.
- Separate **fact**, **vendor claim**, **inference**, and **hypothesis** explicitly. Do not invent revenue, deal size, customer counts, TAM, margins, founder histories or conversion probabilities.
- For missing evidence, say "not independently verified" or "unknown", and propose the smallest way to investigate. Do not silently fill gaps.
- Community commentary may inform frustrations and counter-arguments, but not stand in for representative statistics or validated payments.
- No web/research access: disclose it prominently and supply a hypothesis map, not a "current market research" report.

## Adaptive output contract

The default response should leave the user able to answer:

1. **Who has this problem and what is expensive about it?**
2. **What evidence shows a market exists, and what does not?**
3. **Who is already solving it? What have real buyers done?**
4. **What choices do I have? Why pick one over another?**
5. **How could money be earned, and what remains unproven?**
6. **What is my smallest next experiment and its pass/fail condition?**

Usually provide a source list or a linked source table, and a compact next-steps plan. If a downloadable report was explicitly requested and tooling supports it, create one alongside a concise summary. Never claim background monitoring or a completed customer interview without having actually performed it.

## Quality gate before sending

Check that: (a) one clear commercial decision is addressed; (b) real players have links and roles; (c) demand evidence is not conflated with willingness to pay; (d) meaningful options are compared using the same criteria; (e) founder/customer stories are attributed; (f) prices and timing are dated; (g) recommendation follows from evidence and user constraints; (h) a bounded, testable action comes next. For deep reports, include counter-evidence and unresolved uncertainty rather than forcing an optimistic conclusion.

Use [references/research-brief.md](references/research-brief.md) if the idea needs scoping, and [references/usage-examples.md](references/usage-examples.md) to see how to adapt this workflow across sectors. Answer in the user's preferred language and follow their spelling preferences.
