# Phishing Website Detection App

A web application built using **Streamlit** to detect phishing websites based on various features extracted from URLs. This project is developed as part of learning machine learning and deploying web apps.

## 🔍 About the Project
Phishing websites are malicious sites designed to trick users into revealing sensitive information. This app helps identify such websites using a trained machine learning model.

## 📚 Learnings & Purpose
This project was built to apply:
- Machine learning fundamentals
- Streamlit for web deployment
- Git & GitHub for version control
- Cloud deployment via `streamlit.io`

## 🧠 Algorithm Used
- **Logistic Regression** (or specify actual algorithm if different)
- Trained on a dataset of phishing and legitimate URLs(email_content)
- Features extracted using regex and domain-based heuristics

## 📁 Features Extracted From URLs
- URL length
- Presence of `@`, `//`, or `-`
- Number of subdomains
- Use of HTTPS
- Domain age, etc.

## 🚀 Live App
You can access the deployed app here:
**[Phishing Detection App Live](https://phishing-detection-kp6kgyd4tmvywp9d7jcmaz.streamlit.app/)**

## 🛠 How to Run Locally
```bash
# Clone the repository
git clone https://github.com/varshaethayan/Phishing-detection.git
cd Phishing-detection

# Create virtual environment and activate it (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 📦 Requirements
All dependencies are listed in the `requirements.txt` file.

## 📌 Repository Structure
```
phishing-detection/
├── app.py               # Streamlit application
├── phishing_model.pkl         # Trained ML model
├── requirements.txt     # Python dependencies
├── email_content.csv      # Trained dataset
└── README.md
```

## 👩‍💻 Author
**Varsha Ethayan**  
GitHub: [@varshaethayan](https://github.com/varshaethayan)

## 🧾 License
This project is open-source for educational purposes.
