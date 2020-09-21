from django.db import models

from user.models import User
from core.models.base import BaseEntity
from core.models.location import Location
from service.models.service import Service


class Schedule(BaseEntity):
    name = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.name


class Order(BaseEntity):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='service_order')
    item = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='OrderItem')
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, related_name='order_schedule')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='order_location')
    order_date = models.DateField()
    phone_number = models.IntegerField(default=0)
    status = models.BooleanField(default=False, blank=True)
    address = models.TextField(default=None)

    def __str__(self):
        return self.user.username
