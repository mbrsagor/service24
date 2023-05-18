from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

from service.models.payment import Payment


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = (
            'id', 'name', 'logo'
        )


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = (IsAdminUser,)
    filter_backends = [DjangoFilterBackend]
    search_fields = ['name',]
