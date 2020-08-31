from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import User


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileListView(ListView):
    model = User
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserListView(ListView):
    model = User
    paginate_by = 10
    context_object_name = 'users'
    template_name = 'users/user_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        users = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(users, self.paginate_by)

        try:
            users = paginator.page(page)

        except PageNotAnInteger:
            users = paginator.page(1)
        except EmptyPage:
            users = paginator.page(paginator.num_pages)
        context['users'] = users
        return context
