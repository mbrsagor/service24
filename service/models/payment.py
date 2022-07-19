from django.db import models

from core.models.base import BaseEntity


class Payment(BaseEntity):
    name = models.CharField(max_length=90, unique=True)
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(upload_to='payment/%y/%m/%d', blank=True, null=True)

    def __str__(self):
        return self.name
