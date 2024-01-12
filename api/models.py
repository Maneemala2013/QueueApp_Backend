from django.db import models
from api.utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
)
from rest_framework import serializers

class shop(
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
	appointment_list = serializers.ListField(child=serializers.CharField(max_length=100), allow_null=True)



class user(
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
	appointment_list = serializers.ListField(child=serializers.CharField(max_length=100), allow_null=True)


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
	# user_id = models.CharField(max_length=255, default = "None")
	# shop_id = models.CharField(max_length=255, default = "None")
	user = models.ForeignKey(user, on_delete=models.CASCADE)
	shop = models.ForeignKey(shop, on_delete=models.CASCADE)
	start_time = models.DateTimeField() 
	end_time = models.DateTimeField() 