from django.db import models

from core.models.base import BaseEntity
from user.models import Agent


class Payment(BaseEntity):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, related_name='payment')
    name = models.CharField(max_length=90)
    logo = models.ImageField(upload_to='payment/%y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f"{self.name} use in {self.agent}"
