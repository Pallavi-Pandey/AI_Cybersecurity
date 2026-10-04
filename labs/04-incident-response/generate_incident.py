"""Create the incident log for the lab."""
import csv

events = [
    ("2026-10-05 09:12:40", "email",    "meera", "10.0.4.21",       "Email from billing@vendor-payments.example with link delivered"),
    ("2026-10-05 09:14:03", "email",    "meera", "10.0.4.21",       "User clicked link http://secure-login-verify.example/office365"),
    ("2026-10-05 09:14:31", "firewall", "meera", "10.0.4.21",       "Outbound HTTPS to 185.220.101.7 (secure-login-verify.example)"),
    ("2026-10-05 09:31:12", "vpn",      "meera", "185.220.101.7",   "VPN login success from new country (NL)"),
    ("2026-10-05 09:33:50", "fileserver","meera","185.220.101.7",   "Listed share \\\\fs01\\finance"),
    ("2026-10-05 09:35:02", "fileserver","meera","185.220.101.7",   "Read 214 files in \\\\fs01\\finance\\payroll"),
    ("2026-10-05 09:38:44", "fileserver","meera","185.220.101.7",   "Created archive payroll_2026.zip (412 MB)"),
    ("2026-10-05 09:41:00", "helpdesk", "meera", "-",               "User reports she entered password on unknown page"),
    ("2026-10-05 09:44:19", "firewall", "meera", "185.220.101.7",   "Outbound transfer 412 MB to 185.220.101.7 over HTTPS"),
    ("2026-10-05 09:50:00", "vpn",      "meera", "185.220.101.7",   "VPN session still active"),
    ("2026-10-05 08:55:10", "vpn",      "meera", "10.0.4.21",       "Normal VPN login from office (IN)"),
    ("2026-10-05 09:02:30", "fileserver","rahul","10.0.4.55",       "Read 3 files in \\\\fs01\\sales"),
    ("2026-10-05 09:20:11", "email",    "rahul", "10.0.4.55",       "Email received: team lunch invite"),
]
with open("incident_logs.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["timestamp", "source", "user", "ip", "message"])
    w.writerows(events)
print(f"wrote incident_logs.csv ({len(events)} events, deliberately unsorted)")
