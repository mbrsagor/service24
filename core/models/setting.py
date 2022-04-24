from django.db import models
from .base import BaseEntity


class Setting(BaseEntity):
    site_name = models.CharField(max_length=95)
    is_active = models.BooleanField(default=False)
    copy_write_text = models.CharField(max_length=90, blank=True, null=True)
    logo_upload = models.ImageField(upload_to='setting/logo/%y/%m', blank=True, null=True)
    favicon_upload = models.ImageField(upload_to='setting/favicon//%y/%m', blank=True, null=True)

    def __str__(self):
        return self.site_name
