from djongo import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    _id = models.ObjectIdField()
    email = models.EmailField(blank=True, unique=False)
    phone_number = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.phone_number
