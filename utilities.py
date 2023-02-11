import pandas as pd
import numpy as np
import config
import pickle

with open(config.model_file_path,"rb") as file:
    knn_clf=pickle.load(file)

def diabetes_prediction(data):
    Glucose=float(data['Glucose'])
    BloodPressure=float(data['BloodPressure'])
    SkinThickness=float(data['SkinThickness'])
    Insulin=float(data['Insulin'])
    BMI=float(data['BMI'])
    DiabetesPedigreeFunction=float(data['DiabetesPedigreeFunction'])
    Age=float(data['Age'])

    pred_input=np.array([Glucose ,BloodPressure ,SkinThickness ,Insulin ,BMI ,DiabetesPedigreeFunction ,Age])
    pred_output=knn_clf.predict([pred_input])[0]

    if pred_output==1:
        pred_output="The person has Diabetes"
    elif pred_output==0:
       pred_output="The person has No Diabetes"

    return pred_output









# Glucose=148
# BloodPressure=50
# SkinThickness=35
# Insulin=0
# BMI=33.6
# DiabetesPedigreeFunction=0.627
# Age=50

# pred_input=np.array([Glucose ,BloodPressure ,SkinThickness ,Insulin ,BMI ,DiabetesPedigreeFunction ,Age])
# pred_output=knn_clf.predict([pred_input])[0]