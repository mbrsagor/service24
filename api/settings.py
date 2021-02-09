from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from core.models.setting import Setting


class SettingSerializer(ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'


class ApplicationSettingViewSet(ModelViewSet):
    queryset = Setting.objects.all()
    serializer_class = SettingSerializer
    permission_classes = [IsAuthenticated, ]
