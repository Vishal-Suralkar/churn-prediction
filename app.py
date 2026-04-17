import streamlit as st
import numpy as np
import pickle

# Load model & scaler
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))

st.title("🛒 Customer Churn Prediction")

st.write("Enter customer details:")

recency = st.number_input("Recency (days)")
frequency = st.number_input("Frequency (orders)")
monetary = st.number_input("Monetary (total spend)")

if st.button("Predict"):
    data = np.array([[recency, frequency, monetary]])
    data_scaled = scaler.transform(data)

    prediction = model.predict(data_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Customer likely to churn")
    else:
        st.success("✅ Customer likely to stay")
