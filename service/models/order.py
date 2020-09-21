from django.db import models

from service.utils import OrderStatus
from user.models import User
from core.models.base import BaseEntity
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
    order_date = models.DateField()
    phone_number = models.IntegerField(default=0)
    status = models.IntegerField(choices=OrderStatus.get_choices(), default=OrderStatus.PENDING.value)

    def __str__(self):
        return self.user.username
