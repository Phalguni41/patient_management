
from django.urls import path
from .views import RegisterView, AdminOnlyView, DoctorOnlyView, PatientOnlyView ,PatientUpdateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('doctor-only/', DoctorOnlyView.as_view(), name='doctor-only'),
    path('patient-only/', PatientOnlyView.as_view(), name='patient-only'),
    path('patient/update/', PatientUpdateView.as_view(), name='patient-update'),
]

