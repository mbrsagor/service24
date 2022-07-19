from django.db import models
from django.utils.translation import gettext_lazy as _

from user.models import User
from core.models.base import BaseEntity
from core.models.location import Location
from service.models.service import Service


class Schedule(BaseEntity):
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True, blank=True)
    time = models.TimeField()

    def __str__(self):
        return self.name


class Order(BaseEntity):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='service_order')
    item = models.ForeignKey(Service, on_delete=models.DO_NOTHING, related_name='OrderItem')
    schedule = models.ForeignKey(Schedule, on_delete=models.DO_NOTHING, related_name='order_schedule')
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, related_name='order_location')
    order_date = models.DateField()
    phone_number = models.IntegerField(default=0)

    class STATUS(models.TextChoices):
        PENDING = 'pending', _('Pending')
        CONFIRM = 'confirm', _('Confirm')
        DOING = 'doing', _('Doing')
        REJECT = 'reject', _('Reject')
        DONE = 'done', _('Done')

    status = models.CharField(max_length=10, choices=STATUS.choices, default=STATUS.PENDING, null=True)
    payment_status = models.BooleanField(default=False, blank=True)
    address = models.TextField(default=None)

    def __str__(self):
        return self.user.username

    @property
    def customer(self):
        return self.user.username

    @property
    def addresses(self):
        return self.location.name
