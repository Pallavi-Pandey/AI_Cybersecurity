# 1. AI in Cybersecurity

**Theory time: 45 min** · Hands-on: [lab 01](../labs/01-ai-in-cybersecurity/README.md)

**After this module you can:**
- explain why defenders turned to machine learning, and what it can and cannot do;
- tell supervised from unsupervised learning and pick one for a given security problem;
- read precision, recall and a confusion matrix, and say what a false positive costs;
- name the main ways attackers fool or poison ML systems.

---

## 1. Why defenders need help

A mid-sized company can generate millions of log lines a day: logins, DNS lookups, file accesses, process starts, firewall decisions. A security team of a few analysts cannot read them. Tools turn the logs into **alerts**, and the alerts are then more than people can triage. Surveys of security teams regularly report that a large share of alerts are never investigated, and attackers know it: a quiet intrusion hides in the noise.

Two things grow faster than headcount:
- **Volume** of events and alerts (more cloud services, more devices, more remote work).
- **Attacker speed and automation**: credential-stuffing tools, phishing kits and, increasingly, generative AI (module 2).

AI and machine learning (ML) help with the part that is **repetitive, high volume and pattern-shaped**: sorting, scoring, grouping and spotting the unusual. People are still needed for **judgment and context**: "is this server the payroll database?", "is the CEO really travelling?", "do we shut down production for this?".

> **Say it plainly:** the goal is not to replace the analyst. It is to put the 20 alerts that matter at the top of a queue of 2,000.

**Terms to define on the board:** *AI* (any system doing tasks that seem intelligent), *ML* (AI that learns patterns from data instead of following hand-written rules), *model* (the learned pattern), *feature* (an input number or property the model looks at), *training* (fitting the model to data), *inference* (using it on new data).

---

## 2. Rules versus machine learning

Before ML, detection was mostly **signatures and rules**.

| | Rules / signatures | Machine learning |
|---|---|---|
| Example | "block files whose hash matches known malware"; "alert on 10 failed logins in 5 minutes" | a model that scores every email for phishing, or every login for oddness |
| Strength | precise, fast, **explainable** ("rule 12 fired because...") | finds patterns nobody wrote down; handles variation (reworded phish, new malware family) |
| Weakness | only catches what someone thought of; brittle (change one byte, the hash differs) | needs data; can be wrong in confident ways; harder to explain; can drift |
| Maintenance | people write and tune rules | people collect data, retrain, monitor |
| When it shines | known bad, compliance, clear thresholds | large, messy, changing data where the "bad" is fuzzy |

**Worked example (login failures).** A rule says "alert at 10 failures in 5 minutes". An attacker who tries 1 password every 2 minutes (a "low and slow" attack) never trips it. A model that learns each user's normal pattern may notice "this account usually has zero failures and now has 30 a day from a new country". But the model may also flag the user who just came back from holiday and forgot their password. Each approach has failure modes, so real systems use **both**: rules for the known, ML for the unknown, plus a human to decide (you will see exactly this in lab 03).

---

## 3. How a model learns

### Supervised learning
You give the model **labelled examples** ("this email is phishing", "this one is fine"). It learns what separates the groups and can then label new ones.
- **Good for:** phishing and spam filters, malware classification, malicious URL detection.
- **Needs:** lots of correctly labelled data. In security, labels are costly (an analyst must decide each one) and **attacks are rare**, so the classes are very imbalanced (for example 1 attack in 10,000 events).

### Unsupervised learning
No labels. The model learns what "normal" looks like and flags what is **different** (anomaly detection) or groups similar things (clustering).
- **Good for:** unknown attacks, insider threats, odd network traffic, user behaviour analytics (UEBA).
- **Weakness:** "different" is not the same as "malicious". New but harmless behaviour (a new project, a new office) looks anomalous.

### Walk-through of lab 01 in four steps
1. **Text to numbers:** the model cannot read words, so TF-IDF turns each email into a vector of word weights. Words common in all emails ("the") count less; words special to a few emails count more.
2. **Learn weights:** logistic regression learns a weight per word. "verify" gets a positive weight (towards phishing), "agenda" a negative one.
3. **Score:** add up the weights for an email and squash to a probability from 0 to 1.
4. **Decide:** pick a threshold (for example 0.5). Moving it is a business decision: lower catches more phishing but blocks more real mail.

### Train/test split: why we hold data back
If you test the model on the data it learned from, it looks perfect, like a student who saw the exam questions. So we split: train on most of the data, **test on data the model has never seen**. Even then, if the test set contains near-copies of the training set (as in lab 01, where emails come from a few templates), the score is still inflated. A very high score is a prompt to look for leakage.

---

## 4. Use cases in practice

| Use case | What the model sees | Learning type | Typical difficulty |
|---|---|---|---|
| Phishing and spam filtering | email text, sender, links, headers | supervised | attackers reword constantly |
| Malware classification | file features, API calls, behaviour in a sandbox | supervised | packing and obfuscation |
| UEBA (user and entity behaviour analytics) | logins, access times, data volumes per user | unsupervised | "normal" changes |
| Fraud detection | transactions, device, location | both | rare events, costly mistakes |
| Network anomaly detection | flow volumes, destinations, ports | unsupervised | noisy baselines |
| Vulnerability prioritisation | exploit availability, asset value, exposure | supervised or scoring | far more findings than can be fixed |

Ask the class: *for each row, what would a false positive cost? A false negative?* (Blocked invoice email versus a stolen customer database are very different bills.)

---

## 5. Limits, measurement and adversarial ML

### Measuring: the confusion matrix
Take 1,000 emails, of which 20 are phishing.

| | Model says phishing | Model says legit |
|---|---|---|
| **Really phishing** | **TP** 15 | **FN** 5 (missed attacks) |
| **Really legit** | **FP** 10 (false alarms) | **TN** 970 |

- **Accuracy** = (TP+TN) / all = 985/1000 = 98.5%. Sounds great, but a model that always says "legit" scores 98% too. **Accuracy hides the problem when attacks are rare.**
- **Precision** = TP / (TP+FP) = 15/25 = 60%. "When it alarms, how often is it right?" Low precision means alert fatigue.
- **Recall** = TP / (TP+FN) = 15/20 = 75%. "Of the real attacks, how many did we catch?" Low recall means missed breaches.
- There is a trade-off: raise the threshold and precision goes up while recall goes down. Choose it from the cost of each mistake.

### Why models fail in the field
- **False positives:** each one costs analyst time and trust. Too many and people ignore the tool.
- **Data drift:** behaviour changes (new software, new attack style) and the model's picture of "normal" goes stale. Monitor and retrain.
- **Lack of labelled attack data:** real attacks are rare and secret; many public datasets are old or synthetic, and models trained on them may not transfer.
- **Explainability:** "the model said 0.93" is not enough for an analyst or an auditor. Prefer features and tools that can say *why* (for example the top words in lab 01).
- **Base-rate effect:** if 1 in 10,000 events is an attack, even a model with 99% specificity produces about 100 false alarms for every real attack caught.

### Adversarial ML: the attacker also studies the model
| Attack | What happens | Example |
|---|---|---|
| **Evasion** | craft an input that the model gets wrong at *use* time | rewrite a phish without trigger words; add benign code to malware |
| **Data poisoning** | corrupt the *training* data | mark attacker's emails as "not spam" through a feedback button, so the filter learns to let them through |
| **Model extraction / probing** | query the model to copy it or learn its blind spots | send many test emails and watch which pass |
| **Membership / data leakage** | recover training data from the model | tell whether a record was in the training set |

This is why lab 01 asks you to **break your own model**: if you can fool it in two minutes, an attacker can too.

### Rule of thumb for human-in-the-loop
- **Automate** when mistakes are cheap and reversible (move a suspicious email to a quarantine folder).
- **Keep a human** when mistakes are costly or hard to undo (disable an executive's account, block a production service).

---

## Check your understanding
1. A model scores 99% accuracy on a dataset where 1% of events are attacks. Is it good? What else do you need to know?
2. You must detect a brand-new attack type with no labelled examples. Supervised or unsupervised? Why?
3. Give one example each of evasion and data poisoning against an email filter.
4. When should an AI verdict be auto-actioned, and when should it go to a human?

## Discussion
- Where would you trust a model's verdict automatically, and where would you keep a human in the loop?

## Key takeaways
- ML finds patterns in the data it was given, nothing more.
- Use rules for the known and ML for the unknown; real systems combine both.
- Judge a model by precision and recall in the context of costs, never by accuracy alone.
- Assume an attacker will try to evade and poison your model.

**Further reading:** NIST AI Risk Management Framework; NIST *Adversarial Machine Learning* taxonomy (AI 100-2); scikit-learn user guide, "Model evaluation".
