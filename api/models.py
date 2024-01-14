from django.db import models
from api.utils.model_abstracts import Model
from django_extensions.db.models import (
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
)
from rest_framework import serializers

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
			char with max_length=255 to descript detail of the service, ie the service provider name -> text
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
		("Salon", "Salon"),
        ("Spa & massage", "Spa & massage"),
        ("Beauty", "Beauty"),
        ("Clinic", "Clinic"),
        ("Alternative Therapy", "Alternative Therapy"),
		("None", "None")
	]
	price_range_CHOICES = [
		("N", "N/A"),
		("$", "$"),
        ("$$", "$$"),
        ("$$$", "$$$"),
        ("$$$$", "$$$$"),
	]
	shop_detail = models.TextField(blank=True, default="")
	category = models.CharField(max_length=20, choices=CATEGORIES_CHOICES, default="N")
	phone_number = models.CharField(max_length=20)
	working_hour = models.CharField(max_length=100) # should it be the list of time?
	payment = models.CharField(max_length=100)
	ig_display = models.CharField(max_length=100)
	location = models.CharField(max_length=255)
	farness = models.CharField(max_length=100)
	price_range = models.CharField(max_length=20, choices=price_range_CHOICES, default="N")
	rating = models.FloatField()
	review_num = models.PositiveIntegerField()
	fb = models.CharField(max_length=100)
	profile_image_url = models.TextField(default="")
	available_time_slot = models.TextField(default="0,0,0,0,0,0,0,0,0,0,0,0,0,0,0")

class service(
	TimeStampedModel, 
	ActivatorModel,
	TitleDescriptionModel,
	Model
	):
	duration = models.DurationField()
	price = models.PositiveIntegerField()
	discountedPrice = models.IntegerField(blank=True, default=-1)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

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
		phone_number:
			CharField represented phone number
	"""
	phone_number = models.CharField(max_length=20)


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
		user: 
			char with max_length=255 to descript the user id
		shop: 
			char with max_length=255 to descript the shop id
		start_time: 
			DateTime to descript the starting time of the service
		end_time:
			DateTime to descript the ending time of the service
		remark:


	"""
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
	service_provider = models.CharField(max_length=100)
	date = models.CharField(max_length=100, default="")
	start_time = models.CharField(max_length=20, default="") 
	end_time = models.CharField(max_length=20, default="") 
	remark = models.TextField()