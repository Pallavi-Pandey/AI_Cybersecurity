# 6. Career Roadmap

**Theory time: 35 min** · Hands-on: [lab 06](../labs/06-career-roadmap/README.md)

**After this module you can:**
- compare the main cybersecurity roles and pick two to aim for;
- list the skills each needs and rate your own starting point;
- explain how AI is changing these jobs and which skills keep their value;
- choose practice platforms and certifications for your goal;
- write a 90-day plan and start a portfolio.

---

## 1. The job market in context

Employers in many regions report difficulty finding people with practical, hands-on security skills. Employers look less for a long list of certificates and more for **evidence that you can do the work**: investigate a log, write a script, explain a risk clearly.

AI changes the mix:
- **Routine tasks** (first-pass triage, summarising, boilerplate scripts and queries) are being automated or assisted.
- **Judgment tasks** (deciding what matters, understanding the business, handling an incident, communicating) keep their value and grow in importance.
- **New work appears:** securing AI systems, using AI safely in security teams, and engineering the detections and data pipelines that AI relies on.

So the best position is **security fundamentals + data/scripting skill + knowing how to use and secure AI**.

---

## 2. Roles to aim for

| Role | What you do day to day | Core skills | Good first step |
|---|---|---|---|
| **SOC analyst (Tier 1/2)** | triage alerts, investigate, escalate (module 5) | logs and SIEM, networking, ATT&CK, clear writing | TryHackMe SOC path, Blue Team Labs, a Security+ level cert |
| **Detection engineer** | write and tune rules and models, measure coverage (module 3) | Python, SQL/query languages, Sigma, ML evaluation | build a log anomaly detector (lab 03), publish rules |
| **Incident responder / DFIR** | contain and investigate incidents, forensics (module 4) | OS internals, disk and memory forensics, timelines, calm communication | CTF forensics tasks, timeline projects |
| **Threat hunter / intel analyst** | proactive search, track attacker groups | ATT&CK depth, analysis, scripting, curiosity | write threat reports from public sources |
| **Cloud security engineer** | secure AWS/Azure/GCP: identity, configuration, monitoring | cloud platforms, IAM, infrastructure as code | a cloud associate certification plus a hardening project |
| **Application security engineer** | find and fix flaws in code, secure the software pipeline | web security (OWASP Top 10), code review, dev tools | web CTFs, intentionally vulnerable apps |
| **AI / ML security engineer** | secure ML and LLM systems, red-team AI, build safe pipelines | LLM risks (module 2), Python, ML basics, appsec | OWASP LLM Top 10 labs, prompt injection practice |
| **GRC and risk analyst** | policies, risk assessment, audits, compliance (ISO 27001, SOC 2, DPDP/GDPR) | frameworks, risk methods, communication, now AI governance | ISO 27001 or privacy foundation courses |
| **Security automation / SOAR engineer** | build playbooks and integrations | Python, APIs, SOAR tools | automate an enrichment workflow |

**Choosing:** ask what you enjoy (investigating puzzles, building tools, working with people, policy), and start with an **entry role** such as SOC analyst, helpdesk with security duties, or junior developer with a security focus. Roles are reachable from each other.

---

## 3. Skills to build

### Foundations (everyone)
- **Networking:** IP, DNS, HTTP/HTTPS, TCP vs UDP, ports, firewalls, VPNs. Without this, logs make no sense.
- **Operating systems:** Linux command line and file permissions; Windows basics (accounts, services, event logs, Active Directory idea).
- **Scripting:** Python (files, loops, pandas for data) and Bash; automate small tasks.
- **SQL and data handling:** query, filter and join logs and tables.
- **Security basics:** the CIA triad, authentication vs authorisation, encryption basics, least privilege.

### Security core
- **Web vulnerabilities:** OWASP Top 10 (injection, broken access control, and so on).
- **Logging and SIEM queries:** reading logs, building searches and dashboards.
- **MITRE ATT&CK:** describe and map attacker behaviour (modules 3 and 4).
- **Incident response basics** and writing reports (module 4).
- **Cloud basics:** identity and access management, storage permissions, audit logs.

### AI and data
- **Python data stack:** pandas, numpy, scikit-learn.
- **Model evaluation:** train/test split, precision, recall, confusion matrix (modules 1 and 3).
- **LLM application risks:** prompt injection, data leakage, excessive agency (module 2).
- **Responsible use:** know what you may paste into which tool.

### Soft skills (often decisive)
- **Written communication:** a clear ticket, report or summary is a core output.
- **Calm under pressure**, curiosity, and honest "I don't know, here is how I will find out".
- **Explaining to non-technical people** what risk means in business terms.

---

## 4. How AI will change your daily work

| Before | With AI assistance | Your edge |
|---|---|---|
| read 200 alerts | AI ranks and summarises them | judging what matters, spotting what the model missed |
| write a SIEM query by hand | describe it in words, AI drafts it | verifying and tuning it |
| write a report from scratch | AI drafts from the timeline | accuracy, tone, decisions |
| manual enrichment | automatic | asking the right next question |

Practical habits:
- **Use AI as a fast assistant, then verify.** Models invent facts.
- **Learn the underlying concept** before you rely on the tool; otherwise you cannot spot a wrong answer.
- **Show how you use AI responsibly** (data rules, review) in interviews and your portfolio: employers value it.
- **Stay curious about attacker use of AI**; this is a fast-moving area.

---

## 5. Practice and proof of work

### Practice platforms
- **TryHackMe:** guided rooms and learning paths; good first stop.
- **Hack The Box** and **HTB Academy:** harder, more independent challenges.
- **picoCTF:** beginner-friendly capture-the-flag, free.
- **Blue Team Labs Online, CyberDefenders, LetsDefend:** defender and SOC investigations with real logs.
- **PortSwigger Web Security Academy:** the best free resource for web vulnerabilities.
- **OWASP resources:** Juice Shop, WebGoat, LLM Top 10 material.
- **Home lab:** a couple of virtual machines (Linux, Windows) on your laptop, plus a free or open-source SIEM stack (for example Wazuh or Security Onion) to generate and search your own logs.

### Show your work
- **GitHub projects:** a README stating **problem, approach, result and limitations**, with sample output (the lab 06 checklist). Runs from one command, no secrets, no real personal data.
- **Write-ups:** after each CTF or lab, a short blog or gist of what you did and learned.
- **Small tools:** a log parser, a detection rule set, an alert triage script.
- **Community:** local meetups, Discord groups, conferences, open-source contributions.

### Certifications (a useful signal, not a substitute for skill)
| Level | Examples | Notes |
|---|---|---|
| Entry | CompTIA Security+, Google Cybersecurity Certificate, ISC2 CC | broad basics; often asked for in HR filters |
| Defence | Blue Team Level 1 (BTL1), CompTIA CySA+, Microsoft SC-200 | SOC and analysis |
| Cloud | Microsoft AZ-500, AWS Security Specialty | choose the cloud your target employers use |
| Offence / appsec | CEH, eJPT, OSCP | OSCP is respected and hands-on, and is demanding |
| GRC | ISO 27001 Lead Implementer/Auditor, CISA, CISSP (needs experience) | governance roles |

Pick **one** that matches your target role; certificates cost money and time, and a project often shows more than a second certificate.

---

## 6. Building a 90-day plan

A plan works if it is **specific, dated and measurable**. Example for a beginner aiming at a SOC analyst role:

| Days | Focus | Concrete outputs |
|---|---|---|
| **1 to 30: foundations** | networking, Linux, Python, security basics | 15 hours of Linux/command line practice; finish a networking course; write 3 small Python scripts that read a CSV |
| **31 to 60: defender skills** | SIEM and log analysis, MITRE ATT&CK, two CTF-style labs | complete a SOC learning path; investigate 2 incidents and write them up; map 10 techniques to detection ideas |
| **61 to 90: proof and applications** | one portfolio project, write-ups, applications | publish the log anomaly detector or alert triage tool with a good README; 4 write-ups online; apply to internships and entry roles; practise interviews |

**Habits that make plans succeed:**
- schedule fixed study blocks in your calendar (the lab asks you to book three sessions);
- track progress weekly and adjust, rather than abandon;
- study with a partner or group for accountability;
- **learn in public:** posting your progress builds a network and a record.

### Interview tips
- Be ready to **walk through a project** you built: the problem, your choices, the results, what you would improve.
- Practise explaining a security concept in plain words (for example "what happens when you type a URL?" and "how would you investigate a suspicious login?").
- Be honest about limits (synthetic data, false positives): it shows maturity.

---

## Check your understanding
1. Pick a target role and name three skills it needs that you rate 3 or lower today.
2. Why do employers value a portfolio project?
3. Which tasks in your target role are likely to be assisted by AI, and which will stay human?
4. Write one measurable goal with a date for the next 30 days.

## Key takeaways
- Employers look for proof that you can do the work, not only certificates.
- Combine security fundamentals, scripting or data skill, and knowledge of AI risks.
- Use AI as an assistant and verify; your judgment is the valuable part.
- A specific, dated 90-day plan and one finished portfolio project beat vague ambition.

**Further reading:** NICE Workforce Framework for Cybersecurity (NIST SP 800-181); MITRE ATT&CK for Defenders training; the platforms listed above.
