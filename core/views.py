from django.shortcuts import render
from rest_framework import generics
from .models import CustomUser
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmin, IsDoctor, IsPatient
from .serializers import PatientUpdateSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

class DoctorOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor]

    def get(self, request):
        return Response({"message": "Hello, Doctor!"})

class PatientOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsPatient]

    def get(self, request):
        return Response({"message": "Hello, Patient!"})
class PatientUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated, IsPatient]
    serializer_class = PatientUpdateSerializer

    def get_object(self):
        return self.request.user

