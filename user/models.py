from djongo import models
from django.contrib.auth.models import AbstractUser
from datetime import date
from django.db.models.signals import post_save
from django.dispatch import receiver

from core.models.base import BaseEntity


class User(AbstractUser):
    # _id = models.ObjectIdField()
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
    def get_fullname(self):
        return f"{self.agent.first_name} {self.agent.last_name}"

    @property
    def company_age(self):
        today = date.today()
        return (today - self.age).days


@receiver(post_save, sender=User)
def create_agent_profile(sender, created, instance, **kwargs):
    if created:
        agent_profile = Agent(agent=instance)
        agent_profile.save()


# User Profile
class UserProfile(BaseEntity):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    profession = models.CharField(max_length=60, blank=True, null=True)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=220)
    profile_picture = models.ImageField(upload_to='profile', blank=True, null=True)

    def __str__(self):
        return self.user.username

    @property
    def make_full_name(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        profile = UserProfile(user=instance)
        profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
