from json import JSONDecodeError
from django.http import JsonResponse
from .models import Appointment
from .serializers import AppointmentSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
import uuid
from rest_framework import viewsets

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer