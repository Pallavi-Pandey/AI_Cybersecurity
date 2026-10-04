# 4. Incident Response

**Theory time: 40 min** · Hands-on: [lab 04](../labs/04-incident-response/README.md)

**After this module you can:**
- define an incident and tell it from an event or an alert;
- walk through the NIST incident response lifecycle and say what happens in each phase;
- order containment actions and justify the order;
- build a timeline from several log sources and write a factual incident report;
- say where AI can help and where a human must decide.

---

## 1. Events, alerts and incidents

- **Event:** anything that happens (a login, a file read).
- **Alert:** an event or pattern a tool thinks is suspicious.
- **Incident:** an event that actually or potentially harms confidentiality, integrity or availability of systems or data, and needs a coordinated response.

Most alerts are not incidents. Incident response (IR) is the discipline of handling the ones that are, **calmly, in order, with evidence kept**. Without a plan, people panic, delete evidence, tell the wrong people, or miss a step.

**Common incident types:** phishing and credential theft, ransomware, business email compromise, data breach, insider misuse, malware infection, denial of service, lost or stolen device.

---

## 2. The lifecycle (NIST SP 800-61)

NIST describes four phases. It is a **loop**, not a straight line: lessons from the last incident improve preparation for the next.

### Phase 1: Preparation
Everything you do *before* an incident:
- **People and roles:** who leads (incident commander), who investigates, who talks to management, legal, HR and communications; contact lists that work at 3 a.m.
- **Plan and playbooks:** written steps for common cases (phishing, ransomware, lost laptop), including who may take systems offline.
- **Tools and access:** logging, EDR, a way to isolate a host, forensic tools, a clean place to communicate (attackers may read email).
- **Logging and backups:** you cannot investigate what was never recorded; backups must be tested and offline or immutable.
- **Training and tabletop exercises** (a discussion-based rehearsal; lab 04 is one).

### Phase 2: Detection and analysis
- **Detect:** an alert, a user report (the helpdesk call in lab 04), a third party tip.
- **Triage:** is it real? How serious? Which systems and data? Assign a **severity** (for example low, medium, high, critical) using impact and urgency.
- **Scope:** which accounts, hosts and data are involved? Pivot from the first clue (the user, the IP, the file name) across all log sources.
- **Build a timeline** (below).
- **Document** as you go.

### Phase 3: Containment, eradication, recovery
1. **Containment:** stop the damage from spreading. *Short term:* disable the account, block the IP, isolate the host. *Long term:* temporary fixes while you prepare a clean rebuild.
2. **Eradication:** remove the cause: malware, attacker accounts and persistence, vulnerable software; reset all exposed credentials.
3. **Recovery:** restore systems from clean sources, return to service, **monitor closely** for the attacker coming back.

### Phase 4: Post-incident activity (lessons learned)
Hold a review within days (a "blameless post-mortem"): what happened, what worked, what failed, what changes now. Produce the report, assign **owners and due dates** to follow-up actions, update playbooks and detections. This is where the incident pays for itself.

---

## 3. Containment in detail

Containment is a balance between **stopping the attacker** and **keeping evidence and business running**.

**Typical first actions, in a sensible order for a stolen-password incident:**
1. **Cut the attacker's access:** disable or reset the account and terminate active sessions and tokens. The attacker is using the credentials *right now*, so this comes first.
2. **Cut the channel:** block the attacker's IP and domain at the firewall and proxy. This stops data leaving and protects other users.
3. **Isolate the endpoint** the user clicked on, for investigation (do not wipe it yet).
4. **Hunt for spread:** other recipients of the same email, other logins from the same IP, other accounts on the same device.

**Justify the order by asking:** What is the attacker doing now? What is the fastest action that stops it? What is hardest to undo? Which action destroys evidence?

**Evidence handling:**
- Prefer **isolate** (network quarantine) over **power off** when memory may hold evidence.
- Copy logs and disk images to a safe place; keep a **chain of custody** record (who had it, when).
- **Never** investigate on the compromised machine itself if you can avoid it.
- Record **every action with a timestamp and the person who did it**: it protects the team and supports legal and insurance steps.

**Who must be told:** management, legal and privacy officer (laws such as GDPR and India's DPDP Act, or sector rules, can require notifying regulators and affected people within set times), HR (insider cases), customers and the public (communications team). Do not decide this alone.

---

## 4. Building a timeline

A **timeline** merges events from all sources into one time-ordered story. Each source shows only a slice: email shows the click, the firewall shows the connection, the VPN shows the login, the file server shows what was read. Together they show the attack path.

How to do it well:
1. **Normalise time:** convert everything to one time zone (UTC is common) and note any clock skew.
2. **Sort** by time and label each row with source, user, IP and what happened.
3. **Anchor on the known:** start from the first clue and look both **backwards** (how did it start?) and **forwards** (what next?).
4. **Separate fact from guess:** mark inferences as such.
5. **Mark key moments:** first access, privilege change, data access, data leaving, detection, containment.

In lab 04 the logs are deliberately unsorted: you will see that the story only appears once they are merged, and that the **gap between first detectable signal and actual detection** is where the damage happened.

**Useful measures from the timeline:**
- **Dwell time:** how long the attacker was inside before detection.
- **Time to contain:** from detection to stopping the attacker.
- **Earliest possible detection:** which control *could* have fired, and when. This is the most valuable finding for the lessons-learned step.

---

## 5. Walk-through: phishing to data theft

Use this as the model answer structure.

1. **Initial access:** a phishing email with a link; the user enters her password on a fake login page (ATT&CK **T1566**, credential harvesting).
2. **Use of credentials:** the attacker logs in over VPN from a new country (**T1078** Valid Accounts, **T1133** External Remote Services).
3. **Discovery and collection:** browses file shares, reads many files, builds an archive (**T1083**, **T1039**, **T1560**).
4. **Exfiltration:** sends the archive to a server the attacker controls (**T1041**).
5. **Detection:** the user calls the helpdesk (human reporting), not a tool.
6. **Response:** disable account, kill session, block IP, isolate laptop, find other victims, reset credentials, enable MFA, notify legal and affected staff, write the report.

**Questions to ask at each stage:** what *could* have detected this? What *would* have blocked it? (Email link filtering, MFA, geo-velocity alert, large-transfer alert, data loss prevention.)

---

## 6. Where AI helps (and where it must not decide)

| Task | How AI helps | Keep the human for |
|---|---|---|
| Triage and prioritisation | scores alerts using context | confirming severity |
| Enrichment | looks up IP reputation, user, asset owner automatically | judging relevance |
| Timeline reconstruction | merges and summarises logs, spots gaps | checking facts and gaps |
| Summaries and communication | drafts incident summaries, status updates, post-mortems | accuracy, tone, what to disclose |
| Playbook suggestions | proposes next steps | **approving** anything that changes systems |

**Cautions:**
- A model can **invent** a timestamp or a log line. Check every fact against the source.
- Do not paste sensitive incident data into tools your company has not approved.
- **Automate containment only for well-understood, low-risk, reversible actions** (quarantine an email, block a known-bad IP). Disabling a CEO's account or shutting down a production database needs a person.

---

## 7. Writing the incident report

Facts first, blame never. The structure used in lab 04:
- **Title, severity, who detected and when.**
- **Summary (2 to 3 sentences):** what happened and the impact.
- **Timeline:** time, event, source.
- **Root cause:** why it was possible (no MFA, a filter gap).
- **Impact:** systems, data, users affected.
- **Actions taken** with timestamps.
- **What went well and what did not.**
- **Follow-up actions** with an owner and a due date.

Write for two readers: a technical colleague who needs details, and a manager who reads only the summary.

---

## Check your understanding
1. What is the difference between an alert and an incident?
2. Why is disabling the compromised account usually done before reimaging the laptop?
3. Why can powering off an infected machine be a mistake?
4. Name three pieces of information a good timeline row contains.
5. Which tasks of IR are suitable for full automation, and which are not?

## Exercise (lab 04)
- Walk through a phishing-to-credential-theft scenario: what do you detect, contain, and communicate, and in what order?

## Key takeaways
- A plan made before the incident is worth more than any tool during it.
- Timelines turn noisy logs into a story.
- Containment order matters; document every action with a timestamp.
- Automate low-risk steps, keep people on decisions with impact.
- The report's most valuable part is what you change afterwards.

**Further reading:** NIST SP 800-61 Rev. 2 (and Rev. 3); SANS incident handler's handbook; CISA incident response playbooks.
