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
			'user_id',
			'shop_id',
			'start_time',
			'end_time'
		)