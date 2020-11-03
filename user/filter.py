import django_filters
from .models import Agent


class AgentFilter(django_filters.FilterSet):
    class Meta:
        model = Agent
        fields = ['agent', 'company_name', 'nid_number', 'website']
