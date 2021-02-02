from django.db import models
from .base import BaseEntity


class Setting(BaseEntity):
    site_name = models.CharField(max_length=95)
    logo_upload = models.ImageField(upload_to='setting')
    favicon_upload = models.ImageField(upload_to='setting')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.site_name[:30]
