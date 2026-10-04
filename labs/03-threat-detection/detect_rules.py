"""Rule-based detections. Tune the thresholds marked TODO."""
import pandas as pd

from common import load, report

df, truth = load()
flagged = set()

# Rule 1: brute force = many failures for one user within a short window.
FAIL_THRESHOLD = 10   # TODO: is 10 failures right? try 3 and 30
WINDOW = "5min"
fails = df[df.result == "fail"].set_index("timestamp").sort_index()
for user, g in fails.groupby("user"):
    counts = g["user"].rolling(WINDOW).count()
    if (counts >= FAIL_THRESHOLD).any():
        flagged |= set(df[(df.user == user) & (df.timestamp.between(g.index.min(), g.index.max() + pd.Timedelta("10min")))].index)
        # note: this also flags everything for the user in that span; refine for precision

# Rule 2: logins outside business hours.
OFF_HOURS = (df.timestamp.dt.hour < 6) | (df.timestamp.dt.hour >= 22)   # TODO: adjust hours
flagged |= set(df[OFF_HOURS & (df.result == "success")].index)

# Rule 3: impossible travel = same user, different country, within 1 hour.
df_sorted = df.sort_values("timestamp")
prev_country = df_sorted.groupby("user")["country"].shift()
prev_time = df_sorted.groupby("user")["timestamp"].shift()
IMPOSSIBLE = (prev_country.notna()) & (prev_country != df_sorted.country) & ((df_sorted.timestamp - prev_time) < pd.Timedelta("1h"))
flagged |= set(df_sorted[IMPOSSIBLE].index)

report("rules", flagged, truth)
