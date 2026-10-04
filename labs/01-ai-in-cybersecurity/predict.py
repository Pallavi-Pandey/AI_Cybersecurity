"""Score an email: python predict.py "text" """
import sys

import joblib

model = joblib.load("model.joblib")
text = " ".join(sys.argv[1:])
p = model.predict_proba([text])[0][1]
print(f"phishing probability: {p:.2f} -> {'PHISHING' if p >= 0.5 else 'legit'}")
