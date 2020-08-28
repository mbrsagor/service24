from django.views.generic import ListView
from .models import User


class ProfileListView(ListView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
