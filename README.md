# AI × Cybersecurity: Next-Generation Skills for IT Careers

Industry-focused workshop notes: **4 hours of theory + 4 hours of hands-on labs**.

## What is this about?

**Cybersecurity** is protecting systems, accounts and data from attackers. **AI** (machine learning and generative AI) is now used on both sides: defenders use it to find attacks in huge volumes of data, and attackers use it to make their attacks cheaper and more convincing. This workshop covers both sides, plus the security of AI systems themselves.

## Why does it matter?

- **Too much data, too few people.** Companies produce millions of log events and thousands of alerts a day. Analysts cannot read them all, and a real attack can hide in the noise.
- **Attackers are using AI too.** Phishing emails with perfect grammar, cloned voices and automated reconnaissance make old advice such as "look for spelling mistakes" obsolete.
- **AI systems are a new target.** Chatbots and AI assistants can be tricked (prompt injection) into leaking data or taking actions, so anyone who builds or uses them needs to know the risks.
- **Careers are changing.** Routine security tasks are being assisted by AI, while judgment, investigation and AI-security skills are in demand.

## Use cases: how AI helps (and where it does not)

| Area | What AI does | Example from the labs |
|---|---|---|
| Email security | classifies phishing and spam | Lab 1: phishing classifier, and how attackers evade it |
| Threat detection | spots unusual logins, traffic and behaviour | Lab 3: brute force and impossible travel, rules vs anomaly model |
| Incident response | merges logs into a timeline, drafts summaries and reports | Lab 4: reconstruct a phishing-to-data-theft incident |
| Security operations (SOC) | ranks alerts, enriches them with context, cuts noise | Lab 5: raise the share of real incidents in the top alerts from 50% to over 80% |
| Securing AI apps | guardrails, least privilege, output scanning | Lab 2: prompt injection against an email assistant |
| Defender productivity | explains logs, drafts queries and rules, writes reports (always verified by a person) | Theory modules 2 and 5 |

**How this helps you:** you learn to use AI to work faster and see more, to judge when its answer can be trusted (precision, recall, false positives), to defend against AI-powered attacks, and to secure AI tools that your employer adopts. AI assists the analyst; it does not replace judgment.

## Who is it for?

Students, IT staff and developers starting in or moving towards security. You need basic Python and general IT knowledge. No prior security or machine-learning experience is required.

## What you will be able to do

- Explain how ML detection works and measure it with precision and recall.
- Recognise AI-enabled attacks and prompt injection, and apply layered defences.
- Detect suspicious logins with rules and an anomaly model, and compare them.
- Build an incident timeline, contain an incident in a sensible order and write a report.
- Prioritise a SOC alert queue using context and compute MTTD, MTTR and false-positive rate.
- Plan a career path and publish a first portfolio project.

## Format

Each topic has a theory module and a matching lab. Labs use Python (`pip install -r requirements.txt`) and synthetic data only.

| # | Topic | Theory | Hands-on lab |
|---|---|---|---|
| 1 | AI in Cybersecurity | 45 min | [Phishing email classifier](labs/01-ai-in-cybersecurity/README.md), 50 min |
| 2 | Generative AI & Cyber Threats | 45 min | [Prompt injection and guardrails](labs/02-generative-ai-and-cyber-threats/README.md), 40 min |
| 3 | Threat Detection | 40 min | [Detecting suspicious logins](labs/03-threat-detection/README.md), 50 min |
| 4 | Incident Response | 40 min | [Tabletop and timeline](labs/04-incident-response/README.md), 45 min |
| 5 | Security Operations | 35 min | [Alert triage in a mini SOC](labs/05-security-operations/README.md), 35 min |
| 6 | Career Roadmap | 35 min | [Roadmap and portfolio](labs/06-career-roadmap/README.md), 20 min |
| | **Total** | **240 min** | **240 min** |

## Theory modules

1. [AI in Cybersecurity](theory/01-ai-in-cybersecurity.md)
2. [Generative AI & Cyber Threats](theory/02-generative-ai-and-cyber-threats.md)
3. [Threat Detection](theory/03-threat-detection.md)
4. [Incident Response](theory/04-incident-response.md)
5. [Security Operations](theory/05-security-operations.md)
6. [Career Roadmap](theory/06-career-roadmap.md)

## Suggested flow

Run each theory block followed by its lab (theory then practice), or do all theory first and all labs after. Add breaks as needed on top of the 8 hours of content.

## Facilitators

Solution keys for all six labs, with worked answers and tested solution code, are in [solutions/](solutions/README.md).
