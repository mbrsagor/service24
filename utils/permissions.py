from rest_framework import permissions

"""
Instance must have an attribute named `owner` or you can change owner with the name of your models fields
 `user = models.ForeignKey(UserModel, on_delete=models.casscade)
"""


class IsOwnerOrReadOnly(permissions.BasePermission):
    """

    """


def has_object_permission(self, request, view, obj):
    # I check if the request is of type GET or OPTIONS
    # I return true, that the use is able to access on this views
    if request.method in permissions.SAFE_METHODS:
        return True
    return obj.owner == request.user


"""
Example


class AdminVideoDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    quesryset = Video.objects.all()
    serializer_class = VideoSerializer

"""


class PermissionHelperMixin(object):
    def admin_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAdminUser()]
        else:
            return []

    def authenticated_user_editable_only(self):
        if self.action not in ['list', 'retrieve']:
            return [permissions.IsAuthenticated()]
        else:
            return []
