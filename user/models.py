from djongo import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    _id = models.ObjectIdField()
    email = models.EmailField(blank=True, unique=False)
    phone_number = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.phone_number


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
