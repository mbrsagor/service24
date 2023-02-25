import django_filters
from service.models.service import Service


class ServiceFilter(django_filters.FilterSet):
    """
    Service filter for template engine
    """
    class Meta:
        model = Service
        fields = ['service_name', 'price', 'category', 'location']
