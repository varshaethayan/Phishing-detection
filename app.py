import streamlit as st
import joblib
import re

# Load model
model = joblib.load('phishing_model.pkl')

# Title
st.title("📧 Advanced Phishing Email Detector")
st.markdown("Paste the **From**, **Subject**, and **Body** of an email below.")

# Input fields
from_email = st.text_input("Sender (From):")
subject = st.text_input("Email Subject:")
body = st.text_area("Email Body:")

# Combine inputs for prediction
email_text = from_email + " " + subject + " " + body

# Helper: Check for suspicious URLs
def has_suspicious_url(text):
    urls = re.findall(r'https?://\S+', text)
    return any("login" in url or "verify" in url or "secure" in url for url in urls)

# Helper: Check domain-brand mismatch
def domain_mismatch(email_from, subject):
    known_brands = ['amazon', 'hdfc', 'sbi', 'icici', 'flipkart', 'zomato', 'oyo', 'airtel', 'lic']
    for brand in known_brands:
        if brand in subject.lower() and brand not in email_from.lower():
            return True
    return False

# Predict
if st.button("🚨 Check Email"):
    if email_text.strip():
        prediction = model.predict([email_text])[0]
        confidence = model.predict_proba([email_text])[0][1]  # phishing probability

        # Visual feedback
        st.markdown("### 🔍 Result:")
        if prediction == 1:
            st.error(f"🚨 Likely PHISHING (Confidence: {confidence:.2f})")
        else:
            st.success(f"✅ Legitimate Email (Confidence: {1 - confidence:.2f})")

        # Gauge/progress
        st.markdown("#### Confidence Score")
        st.progress(confidence if prediction == 1 else 1 - confidence)

        # Additional Checks
        st.markdown("### 🛡️ Extra Security Checks:")
        if has_suspicious_url(email_text):
            st.warning("⚠️ Suspicious URL Detected.")
        if domain_mismatch(from_email, subject):
            st.warning("⚠️ Domain and Brand Mismatch.")

    else:
        st.warning("⚠️ Please fill all the fields.")
