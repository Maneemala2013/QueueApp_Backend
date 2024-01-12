from json import JSONDecodeError
from django.http import JsonResponse
from .models import Appointment, Shop, User, service
from .serializers import AppointmentSerializer, ShopSerializer, UserSerializer, ServiceSerializer
from rest_framework.parsers import JSONParser
from rest_framework import views, status
from rest_framework.response import Response
from django.http import Http404
import uuid
from rest_framework import viewsets

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = service.objects.all()
    serializer_class = ServiceSerializer