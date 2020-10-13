from django.db import modelsfrom user.models import Userfrom core.models.base import BaseEntityfrom service.models.service import Servicefrom django.core.exceptions import ValidationErrorfrom django.utils.translation import gettext_lazy as _def rating_validation(value):    if value >= 1 or value <= 5:        raise ValidationError(            _('%(value)s is not valid'),            params={'value': value},        )class Review(BaseEntity):    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='user_review')    review = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, related_name='service_review')    title = models.CharField(max_length=60, blank=True, null=True)    rating = models.PositiveSmallIntegerField(default=1, blank=True, null=True)    review_text = models.TextField(blank=True, null=True)    approved_review = models.BooleanField(default=False)    def __str__(self):        return self.user.username    def approve(self):        self.approved_review = True        self.save()