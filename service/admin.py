from django.contrib import admin

from service.models.service import Service


class ModelService(admin.ModelAdmin):
    list_display = ['owner', 'service_name', 'package_name', 'category', 'location', 'price', 'discount_price', \
                    'quick_delivery_charge', 'created_at']
    search_fields = ['service_name', 'package_name', 'price']
    list_per_page = 8


admin.site.register(Service, ModelService)
