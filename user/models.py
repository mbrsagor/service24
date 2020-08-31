from djongo import models
from django.contrib.auth.models import AbstractUser
from datetime import date

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
    nid_number = models.BigIntegerField(default=0)
    website = models.URLField(blank=True)
    address = models.TextField()
    age = models.DateField()
    contact_number = models.IntegerField(default=0)
    treat_lice = models.CharField(max_length=120, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='agent', blank=True)

    def __str__(self):
        return self.agent.username

    @property
    def company_age(self):
        today = date.today()
        return (today - self.age).days
