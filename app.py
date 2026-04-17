import streamlit as st
import numpy as np
import pickle
import pandas as pd

# -------------------------------
# Load Model
# -------------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(page_title="Churn Prediction", page_icon="🛒", layout="wide")

# -------------------------------
# Header
# -------------------------------
st.markdown("""
<h1 style='text-align: center; color: #4CAF50;'>🛒 Customer Churn Prediction Dashboard</h1>
<p style='text-align: center;'>Predict customer behavior and prevent revenue loss</p>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# Layout (2 columns)
# -------------------------------
col1, col2 = st.columns(2)

# -------------------------------
# Inputs
# -------------------------------
with col1:
    st.subheader("📥 Enter Customer Details")

    recency = st.slider("Recency (days)", 0, 365, 30)
    frequency = st.slider("Frequency (orders)", 0, 50, 5)
    monetary = st.slider("Monetary (₹)", 0, 10000, 1000)

# -------------------------------
# Prediction
# -------------------------------
with col2:
    st.subheader("📊 Prediction Result")

    if st.button("Predict Churn 🚀"):

        data = np.array([[recency, frequency, monetary]])
        data_scaled = scaler.transform(data)

        prediction = model.predict(data_scaled)[0]
        probability = model.predict_proba(data_scaled)[0][1]

        # Animated progress bar
        st.progress(int(probability * 100))

        if prediction == 1:
            st.error(f"⚠️ High Churn Risk ({probability:.2%})")
            st.warning("💡 Suggestion: Offer discounts or retention campaigns")
        else:
            st.success(f"✅ Low Churn Risk ({probability:.2%})")

        # -------------------------------
        # Visualization
        # -------------------------------
        st.subheader("📈 Customer Profile")

        df = pd.DataFrame({
            "Metric": ["Recency", "Frequency", "Monetary"],
            "Value": [recency, frequency, monetary]
        })

        st.bar_chart(df.set_index("Metric"))

        # -------------------------------
        # Customer Segment
        # -------------------------------
        if recency < 30 and frequency > 10:
            st.info("💎 Loyal Customer")
        elif recency > 90:
            st.warning("⚠️ At-Risk Customer")
        else:
            st.info("📊 Regular Customer")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.markdown("<center>Built by Vishal Suralkar 🚀</center>", unsafe_allow_html=True)
