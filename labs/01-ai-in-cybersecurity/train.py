"""Train a TF-IDF + logistic regression phishing classifier."""
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

df = pd.read_csv("emails.csv")
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.25, random_state=1, stratify=df["label"]
)

model = make_pipeline(TfidfVectorizer(ngram_range=(1, 2), min_df=2), LogisticRegression(max_iter=1000))
model.fit(X_train, y_train)

print(classification_report(y_test, model.predict(X_test), target_names=["legit", "phishing"]))

vec, clf = model.named_steps["tfidfvectorizer"], model.named_steps["logisticregression"]
words = vec.get_feature_names_out()
order = clf.coef_[0].argsort()
print("Words pushing towards LEGIT:   ", ", ".join(words[order[:8]]))
print("Words pushing towards PHISHING:", ", ".join(words[order[-8:]]))

joblib.dump(model, "model.joblib")
