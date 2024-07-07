# predictor/admin.py

from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal')
    search_fields = ('age',)
    list_filter = ('sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal')

admin.site.register(Patient, PatientAdmin)
