from django.contrib import admin
from .models import Appointment, Shop


@admin.register(Appointment)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "user_id", "shop_id")

@admin.register(Shop)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "category")