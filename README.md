# ❤️ Heart Disease Prediction App

A **machine learning-powered** web application built with **Streamlit** that predicts the likelihood of heart disease based on medical attributes.  
This project leverages a trained model to provide quick, user-friendly predictions for awareness purposes.

---

## 📌 Table of Contents
- [About the Project](#about-the-project)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Screenshots](#screenshots)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## 📖 About the Project
The **Heart Disease Prediction App** is designed to assess whether a person might be at risk of heart disease based on clinical and lifestyle attributes.  
It uses a dataset from the **UCI Machine Learning Repository** and a trained machine learning model (e.g., Logistic Regression) to make predictions.

This project is intended for **educational and awareness purposes only**, not as a medical diagnosis tool.

---

## 📊 Dataset
- **Source:** [UCI Heart Disease Dataset](https://archive.ics.uci.edu/ml/datasets/heart+disease)
- **Instances:** 303 patients
- **Attributes:** 14 clinical features including:
  - Age
  - Sex
  - Chest Pain Type (cp)
  - Resting Blood Pressure (trestbps)
  - Serum Cholesterol (chol)
  - Fasting Blood Sugar (fbs)
  - Resting ECG (restecg)
  - Maximum Heart Rate Achieved (thalach)
  - Exercise Induced Angina (exang)
  - ST Depression (oldpeak)
  - Slope of ST Segment (slope)
  - Number of Major Vessels (ca)
  - Thalassemia (thal)
  - Target: 0 = No Heart Disease, 1 = Heart Disease

---

## 🛠 Methodology
1. **Data Preprocessing**  
   - Handle missing values  
   - Encode categorical variables  
   - Perform feature scaling if necessary  

2. **Feature Selection**  
   - Correlation analysis  
   - Feature importance techniques  

3. **Model Selection & Training**  
   - Algorithm: Logistic Regression (or other ML models)  
   - Split dataset into train & test sets  
   - Train model on selected features  

4. **Model Evaluation**  
   - Metrics: Accuracy, Precision, Recall, F1-score  
   - Cross-validation for generalization check  

5. **Hyperparameter Tuning**  
   - Grid Search / Random Search for optimization  

6. **Deployment**  
   - Save trained model as `.pkl` file  
   - Build a **Streamlit** UI for predictions  

---

## ✨ Features
- Simple, clean, and interactive **Streamlit UI**.
- Real-time predictions based on user input.
- Responsive design for desktop and mobile.
- Includes **health tips** for high/low risk outcomes.

---

## 🖥 Tech Stack
- **Python 3**
- **Streamlit** (Web App)
- **scikit-learn** (ML Model)
- **Pandas, NumPy** (Data Processing)

---

