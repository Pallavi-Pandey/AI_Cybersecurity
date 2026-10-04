import pandas as pd


def load():
    df = pd.read_csv("logins.csv", parse_dates=["timestamp"], index_col="event_id")
    truth = pd.read_csv("ground_truth.csv", index_col="event_id")["is_attack"].astype(bool)
    return df, truth


def report(name, flagged_ids, truth):
    flagged = set(flagged_ids)
    actual = set(truth[truth].index)
    tp = len(flagged & actual)
    precision = tp / len(flagged) if flagged else 0.0
    recall = tp / len(actual) if actual else 0.0
    print(f"{name}: flagged={len(flagged)} true_attacks_caught={tp}/{len(actual)} precision={precision:.2f} recall={recall:.2f}")
