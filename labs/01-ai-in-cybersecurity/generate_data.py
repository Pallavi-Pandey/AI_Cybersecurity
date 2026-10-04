"""Generate a small synthetic phishing / legitimate email dataset."""
import csv
import random

random.seed(7)

PHISH = [
    "URGENT: your {bank} account is suspended. Verify your password now at {url}",
    "Security alert! Unusual login detected. Click {url} immediately to confirm your identity",
    "You have won a {prize}! Claim now by entering your card details at {url}",
    "Final notice: pay the outstanding invoice today or your account will be closed. Login at {url}",
    "Dear customer, your {bank} KYC is expired. Update details at {url} within 24 hours",
    "Your mailbox is full. Click {url} to avoid losing messages. Act now",
    "Payment failed. Confirm your OTP and password at {url} to avoid penalty",
    "Congratulations, you are selected for a {prize}. Send a processing fee to receive it",
]
LEGIT = [
    "Hi team, the sprint review is moved to {day} at {time}. Agenda attached.",
    "Please find the notes from today's {topic} class. Let me know if you have questions.",
    "Reminder: the {topic} assignment is due on {day}. Submit it on the portal.",
    "Thanks for your help with the {topic} project. Lunch on me this {day}?",
    "Your order has shipped and should arrive by {day}. Track it from your account page.",
    "Meeting notes: we agreed to finish the {topic} report by {day}. Action items below.",
    "Hello, attaching the {topic} slides for tomorrow's session. Feedback welcome.",
    "Can we reschedule our one-on-one to {time} on {day}? Happy to move it if that's hard.",
]
BANKS = ["SBI", "HDFC", "ICICI", "PayPal", "Amazon"]
PRIZES = ["free laptop", "gift card", "lottery prize", "iPhone"]
URLS = ["http://secure-login-verify.example", "http://bit.example/x7Qa", "http://account-update.example/login"]
DAYS = ["Monday", "Tuesday", "Friday", "next week"]
TIMES = ["10 AM", "2 PM", "4:30 PM"]
TOPICS = ["networking", "database", "python", "security", "data science"]


def fill(t):
    return t.format(
        bank=random.choice(BANKS), prize=random.choice(PRIZES), url=random.choice(URLS),
        day=random.choice(DAYS), time=random.choice(TIMES), topic=random.choice(TOPICS),
    )


rows = [(fill(random.choice(PHISH)), 1) for _ in range(300)]
rows += [(fill(random.choice(LEGIT)), 0) for _ in range(300)]
random.shuffle(rows)

with open("emails.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["text", "label"])
    w.writerows(rows)
print(f"wrote emails.csv with {len(rows)} rows")
