from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "user_id", "shop_id")