# Importing necessary libraries
from .models import Patient
# from .models import PatientData
from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from predictor.forms import HeartDiseaseForm
import joblib
import os

# Path to the model file
MODEL_FILE = 'static/heart_disease_rf_model.pkl'

if os.path.exists(MODEL_FILE):
    rf = joblib.load(MODEL_FILE)
else:
    df = pd.read_csv('static/Heart_train.csv')
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1]
    
    rf = RandomForestClassifier(n_estimators=16, criterion='entropy', max_depth=9)
    rf.fit(np.nan_to_num(X), Y)
    
    joblib.dump(rf, MODEL_FILE)

def heart(request):
    value = ''
    
    if request.method == 'POST':
        form = HeartDiseaseForm(request.POST)
        if form.is_valid():
            user_data = np.array([
                form.cleaned_data['age'],
                form.cleaned_data['sex'],
                form.cleaned_data['cp'],
                form.cleaned_data['trestbps'],
                form.cleaned_data['chol'],
                form.cleaned_data['fbs'],
                form.cleaned_data['restecg'],
                form.cleaned_data['thalach'],
                form.cleaned_data['exang'],
                form.cleaned_data['oldpeak'],
                form.cleaned_data['slope'],
                form.cleaned_data['ca'],
                form.cleaned_data['thal']
            ]).reshape(1, -1)
            
            predictions = rf.predict(user_data)
            prediction = int(predictions[0])
            
            Patient.objects.create(
                age=form.cleaned_data['age'],
                sex=form.cleaned_data['sex'],
                cp=form.cleaned_data['cp'],
                trestbps=form.cleaned_data['trestbps'],
                chol=form.cleaned_data['chol'],
                fbs=form.cleaned_data['fbs'],
                restecg=form.cleaned_data['restecg'],
                thalach=form.cleaned_data['thalach'],
                exang=form.cleaned_data['exang'],
                oldpeak=form.cleaned_data['oldpeak'],
                slope=form.cleaned_data['slope'],
                ca=form.cleaned_data['ca'],
                thal=form.cleaned_data['thal'],
                prediction=prediction
            )
            
            if prediction == 2:
                value = 'have'
            elif prediction == 1:
                value = "don't have"

    else:
        form = HeartDiseaseForm()

    return render(request, 'heart.html', {'context': value, 'form': form})

def home(request):
    return render(request, 'home.html')

def view_patients(request):
    patients = Patient.objects.all()  # Retrieve all patient data
    return render(request, 'patient.html', {'patients': patients})
