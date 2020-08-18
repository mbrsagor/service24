from djongo import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    _id = models.ObjectIdField()
    email = models.EmailField(blank=True, unique=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    verification_code = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __str__(self):
        return self.email
