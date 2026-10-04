# 3. Threat Detection

**Theory time: 40 min** · Hands-on: [lab 03](../labs/03-threat-detection/README.md)

## Fundamentals
- Data sources: endpoint, network, identity, cloud, application logs.
- Detection types: signature, heuristic/rule-based, behavioral/anomaly, threat-intel matching.
- Frameworks: MITRE ATT&CK for mapping behavior to tactics and techniques.

## Where AI helps
- Anomaly detection on logins, traffic, and process behavior.
- Clustering and correlating related alerts into one incident.
- Classifying phishing URLs, emails, and malicious files.

## Practical concerns
- Precision vs. recall: the cost of false positives (alert fatigue) vs. false negatives (missed breach).
- Feature quality, baselining "normal", and retraining as behavior drifts.

## Exercise idea
- Given a small login log, flag anomalies (impossible travel, odd hours, brute force) first with rules, then with a simple anomaly model, and compare.
