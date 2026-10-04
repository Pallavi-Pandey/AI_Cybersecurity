# Lab 03: Detecting Suspicious Logins (50 min)

**Goal:** detect brute force and account takeover in login logs, first with rules, then with an anomaly-detection model, and compare.

| Step | Time | What |
|---|---|---|
| Explore data | 10 min | `generate_logins.py`, look at `logins.csv` with pandas |
| Rule-based detection | 15 min | complete and run `detect_rules.py` |
| ML detection | 15 min | run `detect_ml.py` (Isolation Forest) |
| Compare | 10 min | precision/recall of both against the known attacks |

## Steps
1. `python generate_logins.py` creates `logins.csv` (about 3,000 events) and `ground_truth.csv` (which events are attacks). Attacks injected: a brute-force burst, "impossible travel", and off-hours logins.
2. `python detect_rules.py`: fix the TODO thresholds so it catches the attacks without flagging normal users.
3. `python detect_ml.py`: unsupervised model that has never seen the labels.
4. Both scripts print precision and recall against `ground_truth.csv`.

## Tasks
- The starter rules catch every attack but with low precision (many false positives). Find which rule causes most of them and fix it.
- Which attacks does each approach catch or miss?
- Tune the rule thresholds. What happens to false positives when you make the rules stricter?
- Change `contamination` in `detect_ml.py`. How does it trade precision against recall?
- Map each attack to a MITRE ATT&CK technique (Brute Force T1110, Valid Accounts T1078).

## Takeaways
- Rules are precise and explainable but only catch what you thought of.
- Anomaly models find the unexpected but are noisier and need tuning.
- Real SOCs combine both.
