# Lab 01: Phishing Email Classifier (50 min)

**Goal:** train a simple ML model that flags phishing emails, then see where it fails.

| Step | Time | What |
|---|---|---|
| Setup | 10 min | `pip install -r ../../requirements.txt`, check Python runs |
| Train and evaluate | 20 min | run `train.py`, read precision/recall |
| Break it | 20 min | craft emails that fool the model, discuss adversarial ML |

## Steps
1. `python generate_data.py` creates `emails.csv` (synthetic phishing and legitimate emails).
2. `python train.py` trains TF-IDF + logistic regression and prints a report and the top words the model relies on.
3. `python predict.py "your email text here"` scores any text.

## Tasks
- You will likely see 100% scores. Why is that a red flag, not a success? (Hint: look at how `generate_data.py` builds the emails.)
- Which words push an email towards "phishing"? Is that what you expected?
- Write a phishing email the model scores as legitimate (hint: use polite, calm wording and no urgency words). What does this say about relying on keywords alone?
- Write a legitimate email that gets flagged (false positive). What would that cost in a real company?
- Change `test_size` or remove the "urgent" vocabulary from the data. How do the metrics change?

## Takeaways
- ML finds patterns in the data it was given, nothing more.
- Evasion is easy once the attacker knows what the model looks at.
- Always look at precision and recall, not just accuracy.
