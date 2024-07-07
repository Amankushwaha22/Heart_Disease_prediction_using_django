from django.urls import path 
from . import views 
  
urlpatterns = [ 
    path('heart/', views.heart, name="heart"), 
    # path('patient/', views.patient, name='patient'),  # New URL for patient data
    path('patients/', views.view_patients, name='view_patients'),  # URL pattern for viewing patient data
    path('', views.home, name="home"), 
] 