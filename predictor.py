import joblib
import numpy as np
import pandas as pd

class HealthPredictor:
    def __init__(self, model_path = 'my_model.pkl'):
        self.model = joblib.load(model_path)
        self.columns=['PREGNANCIES', 'GLUCOSE', 'BLOODPRESSURE', 'SKINTHICKNESS', 'INSULIN', 'BMI', 'DIABETESPEDIGREEFUNCTION', 'AGE']
    
    def predict(self, features:list):
        df=pd.DataFrame([features], columns=self.columns)
        return self.model.predict(df)[0]