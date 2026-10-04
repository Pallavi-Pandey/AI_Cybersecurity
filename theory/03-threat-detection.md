# 3. Threat Detection

**Theory time: 40 min** · Hands-on: [lab 03](../labs/03-threat-detection/README.md)

**After this module you can:**
- name the main log sources and what each one reveals;
- explain the four detection approaches and when to use each;
- use MITRE ATT&CK to describe what an attacker did;
- explain how rule-based and ML detection work on login data, and why precision and recall trade off;
- describe how to keep detections healthy over time.

---

## 1. What detection is

**Threat detection** is finding evidence of malicious activity in data you already collect, quickly enough to act. An attacker has to *do things* (log in, run programs, copy files, call servers), and every action leaves traces. Detection means collecting those traces, deciding what is suspicious, and raising an alert a human or a playbook can act on.

Detection is never perfect, so the question is always: **which attacks do we want to catch, at what cost in false alarms?**

---

## 2. Data sources (telemetry)

You can only detect what you can see. Typical sources:

| Source | Examples of what it records | Attacks it helps catch |
|---|---|---|
| **Identity** (Active Directory, Entra ID, Okta, VPN) | logins, failures, MFA prompts, password resets, new devices, locations | brute force, password spraying, stolen credentials, impossible travel |
| **Endpoint** (EDR, Windows event logs, Sysmon, auditd) | process starts, command lines, file changes, registry edits, USB use | malware, ransomware, living-off-the-land tools, persistence |
| **Network** (firewall, DNS, proxy, NetFlow, IDS) | connections, destinations, volumes, DNS queries, URLs | command-and-control, data exfiltration, scanning, lateral movement |
| **Cloud** (AWS CloudTrail, Azure Activity, GCP audit) | API calls, role changes, storage access, new keys | misconfigurations, leaked keys, privilege escalation |
| **Application** (web server, database, SaaS audit logs) | requests, errors, queries, exports | web attacks (SQL injection), abuse of business logic, insider data theft |
| **Email** (gateway, mailbox audit) | senders, attachments, links, forwarding rules | phishing, BEC (look for new inbox rules that forward mail out) |

Two practical points:
- **Quality beats quantity.** Logs must have synchronised clocks (NTP), consistent usernames and enough fields. Messy logs make every later step harder (lab 04 shows how a timeline needs them).
- **Collect centrally** in a **SIEM** (security information and event management) so you can search and correlate across sources.

---

## 3. Four ways to detect

### 3.1 Signatures and indicators of compromise (IOCs)
Match against known-bad things: file hashes, malicious IPs and domains, known malware strings. This is the cheapest and most precise method for **known** threats. Threat-intel feeds supply the lists. Weakness: attackers change a hash or a domain in seconds, so IOCs go stale fast (sometimes called the "pyramid of pain": hashes are trivial for the attacker to change, tools and behaviours are painful).

### 3.2 Heuristics and rules
Logic written by a person about **behaviour**: "10 failed logins for one account in 5 minutes", "Word started PowerShell", "login from two countries within an hour". Rules are explainable and testable. Standard formats help share them: **Sigma** (for logs, translates to any SIEM) and **YARA** (for files). Weakness: you only catch what you thought of; thresholds need tuning.

### 3.3 Behavioural and anomaly detection
Learn what is normal for a user, host or network, and flag deviations. It can catch **new** attacks and insiders. Weakness: unusual is not the same as malicious, so it is noisier and needs a baseline that fits.

### 3.4 Threat-intel matching and hunting
Compare your data with intel on attacker groups, tools and techniques. **Threat hunting** is a person proactively asking "if attacker X were here, what would I see?" and searching for it, rather than waiting for an alert.

| Approach | Precision | Finds unknown attacks | Explainable | Effort |
|---|---|---|---|---|
| IOC / signature | very high | no | yes | low |
| Rules | high | only if you foresaw it | yes | medium (tuning) |
| Anomaly / ML | medium to low | yes | harder | high (data, tuning) |
| Hunting | n/a (human led) | yes | yes | high, needs skilled people |

**Layer them:** IOCs and rules for the known, ML for the unexpected, hunting for what slipped through.

---

## 4. MITRE ATT&CK: a common language

**ATT&CK** is a public knowledge base of how real attackers behave, built from observed intrusions. It is organised as:
- **Tactics**: the attacker's goal at a stage (Initial Access, Execution, Persistence, Privilege Escalation, Credential Access, Discovery, Lateral Movement, Collection, Command and Control, Exfiltration, Impact);
- **Techniques** (and sub-techniques): how they do it, each with an ID.

Examples used in this workshop:

| What happened | Tactic | Technique |
|---|---|---|
| Many password guesses on an account | Credential Access | **T1110** Brute Force |
| Attacker logs in with a stolen password | Defence Evasion, Persistence, Initial Access | **T1078** Valid Accounts |
| Email with a malicious link | Initial Access | **T1566** Phishing |
| Data sent to an attacker's server | Exfiltration | **T1041** Exfiltration Over C2 Channel |

Why use it:
- **Describe** an incident in a shared vocabulary in reports (lab 04).
- **Measure coverage:** list which techniques your rules detect and where the blind spots are.
- **Prioritise:** build detections for the techniques your likely attackers use.

---

## 5. Detecting logins: rules and ML side by side (the lab 03 story)

Take a log of logins: time, user, country, success or failure. Three attacks are hiding in it.

### Attack 1: brute force
Pattern: **many failures in a short time** for one account, then maybe a success.
- *Rule:* count failures per user in a sliding window (for example 5 minutes); alert at 10 or more. Flag the success that follows, because it may be the takeover.
- *Weakness:* the attacker slows down to 1 attempt every 2 minutes, or spreads attempts over many accounts (**password spraying**: one common password tried on many users, so no single account shows many failures). Counting per source IP or per password helps.

### Attack 2: impossible travel
Pattern: same user logs in from **India, then Brazil 20 minutes later**. No human travels that fast.
- *Rule:* compare consecutive logins by country and time gap.
- *Weakness:* false positives from VPNs, mobile networks and proxies; false negatives when the attacker uses a proxy in the user's country.

### Attack 3: off-hours login from a new place
Pattern: login at 03:00 from a country never seen for this user.
- *Rule:* flag logins outside working hours.
- *Weakness:* night-shift workers, travelling staff; a per-user baseline is better than one company-wide hour range.

### The ML view
Turn each login into numbers (**features**): hour of day, failure or not, how rare this country is for this user, how many events this user had in the last 10 minutes. An **Isolation Forest** then isolates points that are easy to separate from the rest: rare combinations are isolated in few steps, so they score as anomalous. It never saw labels; it just reports the unusual.

Key setting: **contamination**, the share of events you expect to be anomalous. It directly controls how many alerts you get.

### Comparing the two
- Rules caught everything we wrote a rule for, precisely, and told us *why*.
- The model needed no rules and found the unexpected, but flagged more normal events and needed tuning.
- Real SOCs run both.

---

## 6. Precision, recall and alert fatigue

For any detector, with TP, FP and FN meaning true positives, false positives and false negatives:

- **Precision** = TP / (TP + FP): of the alerts raised, how many were real?
- **Recall** = TP / (TP + FN): of the real attacks, how many did we alert on?

**Worked example.** A detector fires 100 alerts; 20 are real; there were 25 real attacks in total.
Precision = 20/100 = 20%. Recall = 20/25 = 80%. Five attacks were missed, and analysts wasted time on 80 false alarms.

**The trade-off:**
- Stricter threshold: fewer false positives (higher precision) but more misses (lower recall).
- Looser threshold: more attacks caught but more noise.

**Alert fatigue** is the human result: when most alerts are false, analysts stop trusting and checking them, and a real alert gets lost. Therefore the cost of a false positive is not only time, it is lower recall in practice.

**How to choose:** match the threshold to the damage. For ransomware precursors, accept more false alarms. For a low-impact policy violation, favour precision.

**Base-rate warning:** if attacks are 1 in 10,000 events, even a detector that is wrong only 1% of the time on normal events raises about 100 false alerts per real one. Accuracy is a poor metric here; always look at precision and recall.

---

## 7. Keeping detections healthy

- **Baseline "normal":** compare each user or host with itself (per-user country share), not just with the company.
- **Feature quality:** good features beat clever algorithms. "How unusual is this country *for this user*" is more useful than the country code.
- **Drift:** people change jobs, offices open, software updates; models and thresholds go stale. Schedule reviews and retraining.
- **Test detections:** replay known attack data, or run an attack simulation (purple teaming), to prove the rule fires.
- **Document each detection:** purpose, data source, ATT&CK technique, expected false positives, owner, and what the analyst should do next.
- **Tune with evidence:** allow-list known-good sources instead of loosening the rule for everybody.

---

## Check your understanding
1. Which log source would you use to detect password spraying? Which to detect data exfiltration?
2. Why can a rule be precise but still miss a real attack?
3. A rule produces 200 alerts a day and only 4 are real. List three ways to improve it.
4. What does raising the contamination setting do to precision and recall?

## Exercise (lab 03)
- Given a small login log, flag anomalies (impossible travel, odd hours, brute force) first with rules, then with a simple anomaly model, and compare.

## Key takeaways
- You can only detect what you log; make logs complete, centralised and time-synchronised.
- Rules are precise and explainable but only catch what you thought of.
- Anomaly models find the unexpected but are noisier and need tuning.
- Measure with precision and recall, and set thresholds by the cost of each kind of error.
- ATT&CK gives a shared language for what you detect and what you miss.

**Further reading:** MITRE ATT&CK (attack.mitre.org); Sigma rules repository; David Bianco, "The Pyramid of Pain"; scikit-learn documentation on Isolation Forest.
