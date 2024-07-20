from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    medical_history = models.TextField(blank=True)

class MedicalHistoryDocument(models.Model):
    user = models.ForeignKey(CustomUser, related_name='medical_documents', on_delete=models.CASCADE)
    document = models.FileField(upload_to='medical_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)



