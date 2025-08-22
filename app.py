import streamlit as st
import joblib
import re
import string

def clean_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'@\w+|#\w+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\d+', '', text)
    text = text.strip()
    return text


vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("naive_bayes.pkl")

st.title("Toxic Speech Detection")

text_input = st.text_area("Enter text:")

if st.button("Predict"):
    cleaned = clean_text(text_input)
    vectorized = vectorizer.transform([cleaned])
    prediction = model.predict(vectorized)[0]

    

    if prediction == 1:
        st.error("⚠️ Toxic Speech")
    elif prediction == 2:
        st.success("✅ Neutral")
    else:
        st.warning("Unknown Prediction")

