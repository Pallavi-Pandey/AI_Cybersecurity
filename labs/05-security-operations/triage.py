"""Rank alerts and compute SOC metrics. Complete score()."""
import pandas as pd

df = pd.read_csv("alerts.csv", parse_dates=["attack_start", "detected_at", "resolved_at"])


def score(a) -> float:
    """Return a priority score (higher = look at first).

    TODO: combine a.severity_1_5, a.asset_criticality_1_5, a.source_reputation_0_100,
    a.repeat_count and a.is_vip_user. Start simple, e.g. severity * asset criticality,
    then add reputation and see how the ranking improves.
    """
    return a.severity_1_5


df["priority"] = df.apply(score, axis=1)
ranked = df.sort_values("priority", ascending=False)

top_n = len(df) // 5
caught = ranked.head(top_n)["true_incident"].sum()
total = df["true_incident"].sum()
print(f"Top 20% ({top_n} alerts): {caught} are true incidents -> precision {caught / top_n:.0%} (recall {caught / total:.0%})")
print("\nTop 10:")
print(ranked.head(10)[["alert_id", "type", "priority", "true_incident"]].to_string(index=False))

print("\n--- SOC metrics ---")
print(f"MTTD (mean time to detect):  {(df.detected_at - df.attack_start).mean()}")
print(f"MTTR (mean time to resolve): {(df.resolved_at - df.detected_at).mean()}")
print(f"False-positive rate: {(~df.true_incident).mean():.0%}")
print("\nFalse positives by alert type:")
print((~df.true_incident).groupby(df.type).sum().sort_values(ascending=False).to_string())
