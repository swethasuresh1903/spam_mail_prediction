import streamlit as st
import joblib
import re

model = joblib.load(r"C:\Users\Admin\oasis\spam_mail\model\spam_model.pkl")
vectorizer = joblib.load(r"C:\Users\Admin\oasis\spam_mail\model\vectorizer.pkl")

def clean_text(text):
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = ' '.join(text.split())
    return text

st.title("📩 Spam Mail Detector")

input_text = st.text_area("Enter an email message:")

if st.button("Predict"):
    cleaned = clean_text(input_text)
    vec = vectorizer.transform([cleaned])
    pred = model.predict(vec)[0]
    if pred == 1:
        st.error("🚨 This message is **SPAM**!")
    else:
        st.success("✅ This message is **NOT SPAM**.")
