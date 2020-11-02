import django_filters
from django_filters.filterset import CharFilter, ChoiceFilter
from core.models.location import Location


class LocationFilter(django_filters.FilterSet):
    class Meta:
        model = Location
        fields = (
            'name', 'location_type'
        )
