from djongo import models
from django.contrib.auth.models import AbstractUser

from core.models.base import BaseEntity


class User(AbstractUser):
    _id = models.ObjectIdField()
    email = models.EmailField(blank=True, unique=False)
    phone_number = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.username


class Agent(BaseEntity):
    agent = models.OneToOneField(User, on_delete=models.CASCADE, related_name='service_agent')
    company_name = models.CharField(max_length=80)
    website = models.URLField(blank=True)
    address = models.TextField()

    def __str__(self):
        return self.agent.username
