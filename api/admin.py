from django.contrib import admin
from .models import Appointment, Shop, service


@admin.register(Appointment)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "user_id", "shop_id")

@admin.register(Shop)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', "category")

@admin.register(service)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')