import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
model = pickle.load(open('heart_disease_model.pkl', 'rb'))

# Custom CSS for better UI
st.markdown("""
    <style>
        .main {
            background-color: #f4f6f9;
            padding: 2rem;
            border-radius: 10px;
        }
        h1 {
            color: #2E86C1;
            text-align: center;
        }
        .prediction-result {
            padding: 15px;
            border-radius: 10px;
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
        .positive {
            background-color: #ffcccc;
            color: #b30000;
        }
        .negative {
            background-color: #ccffcc;
            color: #006600;
        }
    </style>
""", unsafe_allow_html=True)

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
    prediction = model.predict(input_data)
    return prediction

def app():
    st.title("💓 Heart Disease Prediction App")
    st.write("This app predicts whether a person is likely to have heart disease based on medical parameters.")

    # Layout: two columns for inputs
    col1, col2 = st.columns(2)

    with col1:
        age = st.slider('Age', 20, 100, 50)
        sex = st.selectbox('Sex', [0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
        cp = st.selectbox('Chest Pain Type', [0, 1, 2, 3])
        trestbps = st.slider('Resting Blood Pressure (mm Hg)', 80, 200, 120)
        chol = st.slider('Cholesterol (mg/dL)', 100, 600, 200)
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dL', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        restecg = st.selectbox('Resting Electrocardiographic Results', [0, 1, 2])

    with col2:
        thalach = st.slider('Maximum Heart Rate Achieved', 70, 220, 150)
        exang = st.selectbox('Exercise Induced Angina', [0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
        oldpeak = st.slider('ST Depression (oldpeak)', 0.0, 6.0, 3.0, 0.1)
        slope = st.selectbox('Slope of Peak Exercise ST Segment', [0, 1, 2])
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', [0, 1, 2, 3])
        thal = st.selectbox('Thalassemia', [0, 1, 2, 3])

    if st.button('🔍 Predict'):
        result = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, restecg,
                                       thalach, exang, oldpeak, slope, ca, thal)
        if result == 0:
            st.markdown('<div class="prediction-result negative">✅ No Heart Disease Detected</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="prediction-result positive">⚠️ Heart Disease Detected! Consult a Doctor Immediately</div>', unsafe_allow_html=True)

    # Footer
    st.markdown("---")
    st.markdown("Developed with ❤️ using Streamlit")

if __name__ == '__main__':
    app()
