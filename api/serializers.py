from . import models
from rest_framework import serializers
from rest_framework.fields import CharField

class AppointmentSerializer(serializers.ModelSerializer):

	service_name = CharField(source="title", required=True)
	service_detail = CharField(source="description", required=True)
	
	class Meta:
		model = models.Appointment
		fields = (
			'service_name',
			'service_detail',
			'user',
			'shop',
			'start_time',
			'end_time'
		)

class ShopSerializer(serializers.ModelSerializer):

	shop_name = CharField(source="title", required=True)
	shop_detail = CharField(source="description", required=True)
	# appointment_list = serializers.ListField()
	
	class Meta:
		model = models.Shop
		fields = (
			'shop_name',
			'shop_detail',
			'category',
			'phone_number',
			'working_hour',
			'playment',
			'ig_display',
			'ig_url',
			'location'
		)

class ServiceSerializer(serializers.ModelSerializer):

	service_name = CharField(source="title", required=True)
	service_detail = CharField(source="description", required=True)
	
	class Meta:
		model = models.service
		fields = (
			'service_name',
			'service_detail',
			'duration',
			'price',
		)

class UserSerializer(serializers.ModelSerializer):

	User_name = CharField(source="title", required=True)
	
	class Meta:
		model = models.User
		fields = (
			'User_name',
			'phone_number',
		)