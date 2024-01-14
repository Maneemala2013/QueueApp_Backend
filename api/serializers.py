from rest_framework import serializers
from rest_framework.fields import CharField

from . import models


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    shop_name = CharField(source="title", required=True)

    class Meta:
        model = models.Shop
        fields = (
            "shop_name",
            "shop_detail",
            "category",
            "phone_number",
            "working_hour",
            "payment",
            "ig_display",
            "location",
            "farness",
            "price_range",
            "rating",
            "review_num",
            "fb",
            "profile_image_url",
            "appointment_set",
            "service_set",
            "available_time_slot",
        )


class ServiceSerializer(serializers.ModelSerializer):
    service_name = CharField(source="title", required=True)
    service_detail = CharField(source="description", required=False)

    class Meta:
        model = models.service
        fields = (
            "service_name",
            "service_detail",
            "duration",
            "price",
            "discountedPrice",
            "shop",
        )


class UserSerializer(serializers.ModelSerializer):
    User_name = CharField(source="title", required=True)

    class Meta:
        model = models.User
        fields = (
            "User_name",
            "phone_number",
            "appointment_set",
        )
        
class AppointmentSerializer(serializers.ModelSerializer):
    service_name = CharField(source="title", required=True)
    service_detail = CharField(source="description", required=True)

    class Meta:
        model = models.Appointment
        fields = (
            "service_name",
            "service_detail",
            "user",
            "shop",
            "start_time",
            "end_time",
        )
