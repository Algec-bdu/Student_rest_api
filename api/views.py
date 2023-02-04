from django.shortcuts import render
from rest_framework import generics
from .models import Students
from .serializers import StudentsSerializer

# Create your views here.

class StudentView(generics.CreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
    