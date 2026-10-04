"""Unsupervised anomaly detection with Isolation Forest."""
import pandas as pd
from sklearn.ensemble import IsolationForest

from common import load, report

df, truth = load()

# Feature engineering: turn each login event into numbers.
user_country_share = df.groupby(["user", "country"])["user"].transform("count") / df.groupby("user")["user"].transform("count")
X = pd.DataFrame({
    "hour": df.timestamp.dt.hour,
    "failed": (df.result == "fail").astype(int),
    "country_rarity": 1 - user_country_share,   # how unusual is this country for this user
    "events_in_10min": df.groupby(["user", df.timestamp.dt.floor("10min")])["user"].transform("count"),
}, index=df.index)

CONTAMINATION = 0.03   # TODO: expected fraction of anomalies; try 0.01 and 0.1
model = IsolationForest(contamination=CONTAMINATION, random_state=0).fit(X)
flagged = df.index[model.predict(X) == -1]

report("isolation forest", flagged, truth)
