# 🛒 E-Commerce Customer Churn Prediction

## 📌 Problem Statement

Customer churn is one of the biggest challenges in e-commerce, directly impacting revenue and growth. Businesses often fail to identify customers who are about to stop purchasing.

This project aims to **predict customer churn using behavioral data** and provide **actionable insights to reduce churn and retain high-value customers**.

---

## 🎯 Objective

* Predict customers likely to churn
* Segment customers using RFM analysis
* Estimate potential revenue loss
* Enable targeted retention strategies

---

## 📊 Dataset

* Source: UCI Online Retail Dataset
* ~500,000 transaction records
* Features: CustomerID, InvoiceDate, Quantity, UnitPrice, Country

---

## ⚙️ Tech Stack

* **Python** – Data processing
* **Pandas, NumPy** – Data manipulation
* **Seaborn, Matplotlib** – Visualization
* **Scikit-learn** – Machine Learning
* **SMOTE** – Handling class imbalance
* **Streamlit** – Web app deployment

---

## 🔍 Methodology

### 🧹 Data Cleaning

* Removed missing Customer IDs
* Filtered cancelled transactions
* Eliminated negative quantities

### 🛠️ Feature Engineering

* Created **TotalPrice = Quantity × UnitPrice**
* Built customer-level dataset

### 📈 RFM Analysis

* **Recency** → Days since last purchase
* **Frequency** → Number of transactions
* **Monetary** → Total spending

👉 Used to segment customers based on behavior

---

### ⚠️ Churn Definition

Since the dataset had no churn label:

**Customers inactive for more than 90 days were classified as churned**

---

### 🤖 Model Building

* Algorithm: **Logistic Regression**
* Data split: Train/Test
* Feature scaling applied

---

### ⚖️ Handling Imbalance

* Applied **SMOTE** to balance churn vs non-churn classes
* Improved model learning on minority class

---


## 💡 Business Insights

* High **recency** is the strongest indicator of churn
* A small group of customers contributes most revenue
* Identified **high-value customers at risk**

---

## 💰 Business Impact

* Helps businesses **reduce churn rate**
* Enables **targeted marketing campaigns**
* Prevents potential **revenue loss**

---

## 🚀 Features

* RFM-based segmentation
* Churn prediction model
* SMOTE-based imbalance handling
* Interactive Streamlit web app

---

## 🌐 Live Demo

👉 https://churn-prediction-h3txxjg8bzbyyu6jpudzgi.streamlit.app/

---


## ▶️ How to Run Locally

```
pip install -r requirements.txt
streamlit run app.py
```

---


## 👨‍💻 Author

**Vishal Suralkar**

---

## 🔥 Key Takeaway

This project goes beyond prediction — it delivers **actionable insights that directly impact business revenue and customer retention**.
