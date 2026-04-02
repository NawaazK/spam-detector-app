import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Title
st.title("📩 Spam Message Detector")

# Load dataset
df = pd.read_csv("spam.csv", encoding="latin-1")
df = df[["v1", "v2"]]
df.columns = ["label", "message"]

# Convert labels
df["label"] = df["label"].map({"ham": 0, "spam": 1})

# Train model
X = df["message"]
y = df["label"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

# User input
user_input = st.text_input("Enter a message:")

if user_input:
    input_vec = vectorizer.transform([user_input])
    prediction = model.predict(input_vec)[0]

    if prediction == 1:
        st.error("🚨 Spam detected!")
    else:
        st.success("✅ Not Spam")