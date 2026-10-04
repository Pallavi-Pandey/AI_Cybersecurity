# Lab 04: Incident Response Tabletop and Timeline (45 min)

**Goal:** investigate a simulated phishing-to-data-theft incident across several log sources, build a timeline, and write an incident report.

| Step | Time | What |
|---|---|---|
| Brief | 5 min | read the scenario below |
| Investigate | 20 min | run `timeline.py`, answer the questions |
| Decide | 10 min | containment / eradication / recovery plan |
| Report | 10 min | fill in `report_template.md` |

## Scenario
At 09:41 the helpdesk gets a call: an employee (`meera`) clicked a link in an email and entered her password. Logs from email, VPN, file server and firewall are in `incident_logs.csv` (generate it with `python generate_incident.py`).

## Steps
1. `python generate_incident.py`
2. `python timeline.py` prints the merged, time-ordered timeline. Use `python timeline.py --user meera` or `--source firewall` to filter.

## Questions
1. When did the attacker first gain access, and from where?
2. What did the attacker do next (privilege, lateral movement, data access)?
3. What data was taken and how much? Over what channel?
4. What is the **earliest** point it could have been detected? What detection would have fired?
5. Containment: list the first three actions in order (e.g., disable account, block IP, isolate host) and justify the order.
6. Map the main steps to MITRE ATT&CK (Phishing T1566, Valid Accounts T1078, Exfiltration T1041/T1567).
7. Fill in `report_template.md`. Keep it factual: what, when, impact, actions, lessons.

## Takeaways
- Timelines turn noisy logs into a story.
- Containment order matters; document every action with a timestamp.
- The report's most valuable part is what you change afterwards.
