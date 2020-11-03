import django_filters
from service.models.service import Service


class ServiceFilter(django_filters.FilterSet):
    class Meta:
        model = Service
        fields = ['service_name', 'price', 'package_name']
