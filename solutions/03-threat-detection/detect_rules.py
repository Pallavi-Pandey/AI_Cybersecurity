"""Rule-based detections: SOLUTION (precise brute-force rule, tuned thresholds)."""
import pandas as pd

from common import load, report

df, truth = load()
flagged = set()

# Rule 1: brute force = many failures for one user within a short window.
# The starter flagged EVERY event between a user's first and last failure. user05 has a
# few normal failures early in the month, so that span covered ~the whole month.
# Fix: flag only the failures inside the burst, plus a success right after it
# (a success after a burst of failures is the likely account takeover).
FAIL_THRESHOLD = 10
WINDOW = pd.Timedelta("5min")
AFTER = pd.Timedelta("10min")
fails = df[df.result == "fail"].sort_values("timestamp")
for user, g in fails.groupby("user"):
    ts = g.timestamp
    in_window = ts.apply(lambda t: ((ts > t - WINDOW) & (ts <= t)).sum())   # failures in the 5 min up to t
    burst = g[in_window >= FAIL_THRESHOLD]
    if burst.empty:
        continue
    flagged |= set(burst.index)
    # failures that belong to the burst (inside the window of any burst event)
    for t in burst.timestamp:
        flagged |= set(g[(ts > t - WINDOW) & (ts <= t)].index)
    last = burst.timestamp.max()
    user_events = df[df.user == user]
    flagged |= set(user_events[(user_events.result == "success") & user_events.timestamp.between(last, last + AFTER)].index)

# Rule 2: logins outside business hours (22:00-06:00). Few real users log in then, and
# every hit in this data is an attack. In real life add a per-user allow-list (night-shift staff).
OFF_HOURS = (df.timestamp.dt.hour < 6) | (df.timestamp.dt.hour >= 22)
flagged |= set(df[OFF_HOURS & (df.result == "success")].index)

# Rule 3: impossible travel = same user, different country, within 1 hour.
df_sorted = df.sort_values("timestamp")
prev_country = df_sorted.groupby("user")["country"].shift()
prev_time = df_sorted.groupby("user")["timestamp"].shift()
IMPOSSIBLE = (prev_country.notna()) & (prev_country != df_sorted.country) & ((df_sorted.timestamp - prev_time) < pd.Timedelta("1h"))
flagged |= set(df_sorted[IMPOSSIBLE].index)

report("rules (solution)", flagged, truth)
