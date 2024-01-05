import pickle
import streamlit as st

heart_model = pickle.load(open("heart_disease_model.sav", "rb"))

st.title("Heart Disease Prediction ❤️")

age = st.number_input("Age", value=None)
sex = st.number_input("Sex", value=None)
cp = st.number_input("Chest Pain", value=None)
trestbps = st.number_input("Resting Blood Pressure", value=None)
chol = st.number_input("Serum Cholersotral in mg/dl", value=None)
fbs = st.number_input("Fasting Blood Sugar", value=None)
restecg = st.number_input("Resting ECG results", value=None)
thalach = st.number_input("Maximum Heart Rate", value=None)
exang = st.number_input("Exercise Induced Angina", value=None)
oldpeak = st.number_input("ST depression induced by exercise", value=None)
slope = st.number_input("Slope of Peak exercise ST segment", value=None)
ca = st.number_input("Number of Major Vessels (0-3)", value=None)
thal = st.number_input("Thal: 0 = normal; 1 = fixed defect; 2 = reversible defect", value=None)

heart_diagnosis = ""

if st.button("Heart Disease Result"):
    heart_prediction = heart_model.predict(
        [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

    if heart_prediction[0] == 1:
        heart_diagnosis = "The person has a Heart Disease"
    else:
        heart_diagnosis = "The person does not have a Heart Disease"

st.success(heart_diagnosis)
