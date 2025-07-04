import streamlit as st
from predictor import HealthPredictor
from patient import Patient
from database import DataBaseHandler
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db = DataBaseHandler(host=db_host, user=db_user, password=db_pass, database=db_name)
db.create_table()

predictor = HealthPredictor()

st.title("Diabetes Risk Predictor")

name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=0, max_value=120)
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=30)
glucose = st.number_input("Glucose Level", min_value=0.0, max_value=300.0)
bp = st.number_input("Blood Pressure", min_value=0.0, max_value=200.0)
skinThickness = st.number_input("skinThickness", min_value=0.0, max_value=100.0)
insulin = st.number_input("Insulin", min_value=0.0, max_value=900.0)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0)
dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=3.0)

if st.button("Predict"):
    patient = Patient(name, age, pregnancies, glucose, bp, skinThickness, insulin, bmi, dpf)
    features = [age, pregnancies, glucose, bp, skinThickness, insulin, bmi, dpf]
    prediction = str(predictor.predict(features))
    
    db.insert_patient(patient, prediction)
    if prediction=='1':
        st.error(f"Prediction: Has diabetes!")
    else:
        st.success(f"Prediction: Does not have diabetes🎉")