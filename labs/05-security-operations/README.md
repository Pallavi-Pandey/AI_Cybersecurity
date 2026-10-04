# Lab 05: Alert Triage in a Mini SOC (35 min)

**Goal:** act as a Tier-1 analyst with a queue of 200 alerts. Build a scoring function that ranks them, enrich with context, and measure the SOC the way managers do.

| Step | Time | What |
|---|---|---|
| Generate queue | 5 min | `python generate_alerts.py` |
| Build the scoring | 15 min | complete the TODOs in `triage.py` |
| Metrics | 10 min | MTTD / MTTR / false-positive rate |
| Discuss | 5 min | where would an LLM assistant help, and where not? |

## Steps
1. `python generate_alerts.py` creates `alerts.csv` (type, severity, asset criticality, source reputation, whether the user is a VIP, true/false positive label, timestamps).
2. In `triage.py` write `score(alert)`: combine severity, asset criticality, threat-intel reputation, and repeat-count into a priority score. Run it to see the top 10 and what share of the top 20% are real incidents.
3. The script prints MTTD, MTTR and false-positive rate. Which alert types create most of the noise?

## Tasks
- Improve the ranking until at least 70% of your top 20% of alerts are true incidents (the plain-severity baseline is about 50%).
- Pick the noisiest alert type. Propose a tuning change (threshold, allow-list, correlation) and estimate analyst hours saved.
- Draft the prompt you would give an LLM to summarize an alert for an analyst. What data must you NOT send to an external model?

## Takeaways
- Prioritization is context (asset value, reputation), not just severity.
- Metrics need definitions: MTTD = detection time minus attack start; MTTR = resolution time minus detection.
- Automate enrichment first, response last.
