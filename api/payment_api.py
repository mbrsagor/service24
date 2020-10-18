from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

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
