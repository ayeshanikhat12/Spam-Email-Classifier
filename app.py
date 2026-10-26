
import streamlit as st
import joblib

st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="centered"
)

model = joblib.load("models/spam_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

st.markdown("""
<style>
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"] {
    background: #000000 !important;
}

.block-container {
    max-width: 800px;
    padding-top: 2rem;
}

h1, p, label, [data-testid="stCaptionContainer"] {
    color: #CCCCCC !important;
}

.stTextArea textarea {
    background: #333333 !important;
    color: #FFFFFF !important;
    border: 1px solid #555555 !important;
    border-radius: 10px !important;
}

.stButton > button {
    width: 100%;
    background: #404040 !important;
    color: #FFFFFF !important;
    border: 1px solid #666666 !important;
    border-radius: 8px;
    height: 48px;
}

.result-box {
    padding: 24px;
    border-radius: 10px;
    margin-top: 20px;
    color: #000000 !important;
    font-size: 18px;
    font-weight: bold;
}

.result-box h3,
.result-box p {
    color: #000000 !important;
}

.spam {
    background: #DC3545 !important;
}

.ham {
    background: #198754 !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Spam Email Classifier")
st.caption("Machine Learning Project | Codec Technologies")
st.write("Enter an email to check its classification.")

email = st.text_area(
    "Email content",
    height=200,
    placeholder="Paste your complete email here..."
)

if st.button("CHECK EMAIL"):
    if email.strip():
        email_tfidf = tfidf.transform([email])
        prediction = model.predict(email_tfidf)[0]

        if prediction == "spam":
            st.markdown("""
            <div class="result-box spam">
                <h3>SPAM EMAIL DETECTED</h3>
                This email may be unwanted or suspicious.
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-box ham">
                <h3>LEGITIMATE EMAIL (HAM)</h3>
                The model classified this email as legitimate.
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Please enter an email first.")

st.caption("Note: This is a machine learning model and may not be 100% accurate. Always exercise caution when dealing with emails.")
