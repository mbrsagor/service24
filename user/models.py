from django.db.models import Q
from django.conf import settings
from django.utils.functional import cached_property
from djongo import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    _id = models.ObjectIdField()
    email = models.EmailField(blank=True, unique=False)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, default=None, null=True, blank=True)
    active = models.BooleanField(default=True)
    verification_code = models.CharField(max_length=255, default=None, null=True, blank=True)

    def __is_in_group(self, group):
        return self.groups.filter(name=group).exists()

    @cached_property
    def is_agent(self):
        return self.__is_in_group(settings.AGENT_GROUP)

    @cached_property
    def is_editor(self):
        return self.__is_in_group(settings.EDITOR_GROUP)

    @cached_property
    def is_moderator(self):
        return self.__is_in_group(settings.MODERATOR_GROUP)

    @cached_property
    def is_admin(self):
        return self.is_superuser or self.__is_in_group(settings.ADMIN_GROUP)

    @cached_property
    def is_user(self):
        return self.__is_in_group(settings.USER_GROUP)

    @cached_property
    def get_children(self):
        if self.is_superuser:
            return User.objects.all()
        users = User.objects.filter(parent=self)
        if self.is_moderator or self.is_editor:

            users = User.objects.filter(Q(parent__in=users) | Q(pk=[o.pk for o in users]))
            if self.is_editor:
                users = User.objects.filter(Q(parent__in=users) | Q(pk=[o.pk for o in users]))
        return users
