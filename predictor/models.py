from django.db import models

class Patient(models.Model):
    age = models.FloatField()
    sex = models.FloatField()
    cp = models.FloatField()
    trestbps = models.FloatField()
    chol = models.FloatField()
    fbs = models.FloatField()
    restecg = models.FloatField()
    thalach = models.FloatField()
    exang = models.FloatField()
    oldpeak = models.FloatField()
    slope = models.FloatField()
    ca = models.FloatField()
    thal = models.FloatField()
    prediction = models.IntegerField(default=1)  # Default value is set to 1

    def __str__(self):
        return f"Patient {self.id} - Prediction: {'Heart Disease' if self.prediction == 2 else 'No Heart Disease'}"
