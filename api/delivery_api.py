from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from service.models.delivery import Delivery

class DeliverySerializer(ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'


class DeliveryViewSet(ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAdminUser, ]

    def get_queryset(self):
        pass
