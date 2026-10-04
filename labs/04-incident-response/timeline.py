"""Print the incident timeline: python timeline.py [--user NAME] [--source NAME]"""
import argparse

import pandas as pd

ap = argparse.ArgumentParser()
ap.add_argument("--user")
ap.add_argument("--source")
args = ap.parse_args()

df = pd.read_csv("incident_logs.csv", parse_dates=["timestamp"]).sort_values("timestamp")
if args.user:
    df = df[df.user == args.user]
if args.source:
    df = df[df.source == args.source]

for _, r in df.iterrows():
    print(f"{r.timestamp:%H:%M:%S}  {r.source:<10} {r.user:<6} {r.ip:<16} {r.message}")
