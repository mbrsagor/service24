from django.contrib import admin

from service.models.service import Service
from service.models.order import Order, Schedule
from service.models.review import Review
from service.models.payment import Payment
from service.models.delivery import Delivery


class ModelService(admin.ModelAdmin):
    list_display = ['owner', 'service_name', 'package_name', 'category', 'location', 'price', 'discount_price', \
                    'quick_delivery_charge', 'created_at']
    search_fields = ['service_name', 'package_name', 'price']
    list_per_page = 8


admin.site.register(Service, ModelService)


class ModelOrder(admin.ModelAdmin):
    list_display = ['id', 'user', 'item', 'schedule', 'phone_number', 'status', 'payment_status', 'location',
                    'created_at']
    search_fields = ['id', 'phone_number']
    list_filter = ['user', 'phone_number']
    list_display_links = ['user']
    list_per_page = 8


admin.site.register(Order, ModelOrder)


class ModelSchedule(admin.ModelAdmin):
    list_display = ['id', 'name', 'time', 'created_at', 'updated_at']
    search_fields = ['name', 'time']
    list_display_links = ['name', ]
    list_editable = ['time']
    list_filter = ['name', 'time']
    list_per_page = 8


admin.site.register(Schedule, ModelSchedule)


class ModelReview(admin.ModelAdmin):
    list_display = ['id', 'user', 'service', 'title', 'rating']
    search_fields = ['title']
    list_editable = ['rating']
    list_filter = ['title', 'service', 'rating']
    list_display_links = ['id', 'user']
    list_per_page = 8


admin.site.register(Review, ModelReview)

admin.site.register(Payment)


class ModelDelivery(admin.ModelAdmin):
    list_display = ['id', 'name', 'delivery_charge', 'status', 'delivery_man', 'delivery_service']
    search_fields = ['name', 'delivery_service', 'delivery_man']
    list_editable = ['delivery_charge']
    list_filter = ['name', 'delivery_charge', 'status']
    list_display_links = ['id', 'name']
    list_per_page = 8

admin.site.register(Delivery, ModelDelivery)
