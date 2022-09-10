from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

UserModel = get_user_model()


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
            return
        except UserModel.MultipleObjectsReturned:
            user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by(
                'id').first()

        if user.check_password(password) and self.user_can_authenticate(user):
            return user


class ActiveAccountBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = UserModel.objects.get(phone_number=username)
        if user.check_password(password) and self.user_can_authenticate(user) and user.is_active:
            return user
