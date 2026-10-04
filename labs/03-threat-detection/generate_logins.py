"""Generate synthetic login events with injected attacks."""
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
users = [f"user{i:02d}" for i in range(1, 21)]
home = {u: rng.choice(["IN", "IN", "IN", "US"]) for u in users}
rows = []

# Normal behaviour: office hours, home country, mostly successful.
for _ in range(2900):
    u = rng.choice(users)
    ts = pd.Timestamp("2026-09-01") + pd.Timedelta(days=int(rng.integers(0, 28)), hours=int(rng.integers(8, 19)), minutes=int(rng.integers(0, 60)))
    rows.append((ts, u, home[u], "success" if rng.random() > 0.04 else "fail", 0))

# Attack 1: brute force burst against one user.
t0 = pd.Timestamp("2026-09-15 02:10")
for i in range(60):
    rows.append((t0 + pd.Timedelta(seconds=5 * i), "user05", "RU", "fail", 1))
rows.append((t0 + pd.Timedelta(minutes=6), "user05", "RU", "success", 1))

# Attack 2: impossible travel (IN login then US login 20 min later).
t1 = pd.Timestamp("2026-09-20 11:00")
rows.append((t1, "user09", "IN", "success", 0))
rows.append((t1 + pd.Timedelta(minutes=20), "user09", "BR", "success", 1))

# Attack 3: off-hours logins from a new country.
for i in range(5):
    rows.append((pd.Timestamp("2026-09-24 03:00") + pd.Timedelta(minutes=7 * i), "user14", "CN", "success", 1))

df = pd.DataFrame(rows, columns=["timestamp", "user", "country", "result", "is_attack"]).sort_values("timestamp").reset_index(drop=True)
df.index.name = "event_id"
df.drop(columns="is_attack").to_csv("logins.csv")
df[["is_attack"]].to_csv("ground_truth.csv")
print(f"wrote logins.csv ({len(df)} events, {int(df.is_attack.sum())} attack events)")
