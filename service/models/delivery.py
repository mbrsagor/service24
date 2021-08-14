from core.models.base import BaseEntity
from core.models.location import Location
from django.db import models
from user.models import User

from service.models.service import Service

# from core.utils import DeliveryStatus


class Delivery(BaseEntity):
    name = models.CharField(max_length=30)
    delivery_charge = models.IntegerField(default=0)
    # status = models.IntegerField(choices=DeliveryStatus.get_choices().PROGRESS, default=DeliveryStatus.get_choices().PROGRESS)
    delivery_man = models.ForeignKey(User, on_delete=models.CASCADE, related_name='delivery_man')
    delivery_service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name='delivery_item', blank=True, null=True)
    address = models.ForeignKey(Location, on_delete=models.SET_NULL, related_name='delivery_address', blank=True, null=True)

    def __str__(self):
        return self.name
