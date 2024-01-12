from django.db import models
from api.utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
)
from rest_framework import serializers

class service(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):
	duration = models.DurationField()
	price = models.IntegerField()


class Shop(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):
	"""
	field:
		id: 
			uuid of the ticket
		created: 
			CreationDateTimeField of created Time
		modified: 
			ModificationDateTimeField of modified Time
		title: 
			char with max_length=255 to descript the service name
		description: 
			char with max_length=255 to descript detail of the service, ie the service provider name
		user_id: 
			char with max_length=255 to descript the user id
		shop_id: 
			char with max_length=255 to descript the shop id
		start_time: 
			DateTime to descript the starting time of the service
		end_time:
			DateTime to descript the ending time of the service
	"""
	CATEGORIES_CHOICES = [
		("sl", "Salon"),
        ("sp", "Spa"),
        ("bt", "Beauty"),
        ("cn", "Clinic"),
        ("Alt", "Alternative Therapy"),
		("N", "None")
	]
	category = models.CharField(max_length=20, choices=CATEGORIES_CHOICES, default="N")
	phone_number = models.CharField(max_length=20)
	working_hour = models.CharField(max_length=100) # should it be the list of time?
	playment = models.CharField(max_length=100)
	ig_display = models.CharField(max_length=100)
	ig_url = models.URLField()
	location = models.CharField(max_length=100)
	# appointment_list = serializers.ListField(models.CharField(max_length=100), allow_null=True)
	# service_list = serializers.ListField(child=models.ForeignKey(service, on_delete=models.CASCADE), allow_null=True)

class User(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):
	"""
	field:
		id: 
			uuid of the ticket
		created: 
			CreationDateTimeField of created Time
		modified: 
			ModificationDateTimeField of modified Time
		title: 
			char with max_length=255 to descript the service name
		description: 
			char with max_length=255 to descript detail of the service, ie the service provider name
		user_id: 
			char with max_length=255 to descript the user id
		shop_id: 
			char with max_length=255 to descript the shop id
		start_time: 
			DateTime to descript the starting time of the service
		end_time:
			DateTime to descript the ending time of the service
	"""
	phone_number = models.CharField(max_length=20)
	# appointment_list = serializers.ListField(child=serializers.CharField(max_length=100), allow_null=True)


class Appointment(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):
	"""
	field:
		id: 
			uuid of the ticket
		created: 
			CreationDateTimeField of created Time
		modified: 
			ModificationDateTimeField of modified Time
		title: 
			char with max_length=255 to descript the service name
		user_id: 
			char with max_length=255 to descript the user id
		shop_id: 
			char with max_length=255 to descript the shop id
		start_time: 
			DateTime to descript the starting time of the service
		end_time:
			DateTime to descript the ending time of the service
	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	service_provider = models.CharField(max_length=100)
	start_time = models.DateTimeField() 
	end_time = models.DateTimeField() 
	remark = models.CharField(max_length=255)