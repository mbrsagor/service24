from django.contrib import admin

from service.models.service import Service
from service.models.order import Order, Schedule


class ModelService(admin.ModelAdmin):
    list_display = ['owner', 'service_name', 'package_name', 'category', 'location', 'price', 'discount_price', \
                    'quick_delivery_charge', 'created_at']
    search_fields = ['service_name', 'package_name', 'price']
    list_per_page = 8


admin.site.register(Service, ModelService)


class ModelOrder(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'schedule', 'phone_number', 'created_at']
    search_fields = ['id', 'phone_number']
    list_filter = ['user', 'phone_number']
    list_display_links = ['user']
    list_per_page = 8


admin.site.register(Order, ModelOrder)
admin.site.register(Schedule)
