"""Generate a synthetic alert queue."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(3)
N = 200
types = ["malware", "phishing", "brute_force", "port_scan", "policy_violation", "data_exfil"]
noise_weight = {"port_scan": 0.9, "policy_violation": 0.85, "brute_force": 0.6, "phishing": 0.4, "malware": 0.35, "data_exfil": 0.25}

t = rng.choice(types, N, p=[0.12, 0.18, 0.2, 0.25, 0.15, 0.10])
true_incident = np.array([rng.random() > noise_weight[x] for x in t])
severity = np.where(true_incident, rng.integers(2, 6, N), rng.integers(1, 5, N))
asset_crit = np.where(true_incident, rng.integers(2, 6, N), rng.integers(1, 5, N))
rep = np.where(true_incident, rng.integers(40, 100, N), rng.integers(0, 70, N))
start = pd.Timestamp("2026-10-05 08:00") + pd.to_timedelta(rng.integers(0, 600, N), unit="min")
detect = start + pd.to_timedelta(rng.integers(1, 120, N), unit="min")
resolve = detect + pd.to_timedelta(rng.integers(10, 480, N), unit="min")

df = pd.DataFrame({
    "alert_id": range(1, N + 1), "type": t, "severity_1_5": severity,
    "asset_criticality_1_5": asset_crit, "source_reputation_0_100": rep,
    "repeat_count": rng.integers(1, 15, N), "is_vip_user": rng.random(N) < 0.1,
    "attack_start": start, "detected_at": detect, "resolved_at": resolve,
    "true_incident": true_incident,
})
df.to_csv("alerts.csv", index=False)
print(f"wrote alerts.csv ({N} alerts, {int(true_incident.sum())} true incidents)")
