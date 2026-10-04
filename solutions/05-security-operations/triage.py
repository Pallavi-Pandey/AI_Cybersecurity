"""Rank alerts and compute SOC metrics: SOLUTION (context-aware score)."""
import pandas as pd

df = pd.read_csv("alerts.csv", parse_dates=["attack_start", "detected_at", "resolved_at"])


def score(a) -> float:
    """Priority = how bad if real x how likely it is real.

    - severity * asset criticality: impact if the alert is true
    - source reputation: threat-intel signal, the strongest hint that it is real
    - repeat_count: persistence (capped so one noisy source cannot dominate)
    - VIP user: small bump, an attack on a VIP is costlier
    """
    impact = a.severity_1_5 * a.asset_criticality_1_5            # 1..25
    likelihood = a.source_reputation_0_100 / 100                 # 0..1
    persistence = 1 + min(a.repeat_count, 10) / 20               # 1..1.5
    vip = 1.2 if a.is_vip_user else 1.0
    return impact * likelihood * persistence * vip


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
