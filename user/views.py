from django.views.generic import ListView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, render
from django.contrib import messages

from .models import User
from .forms import CreateAgentFrom


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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserDeleteView(View):

    def get(self, request, username):
        obj = User.objects.get(username=self.kwargs['username'])
        obj.delete()
        return redirect('/user/user-list/')


@login_required(login_url='/login/')
def create_agent_view(request):
    form = CreateAgentFrom()
    if request.method == 'POST':
        form = CreateAgentFrom(request.POST or request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save(request.user)
            messages.add_message(request, messages.INFO, "Agent profile has been created.")
            return redirect('user/profile/')
        else:
            messages.add_message(request, messages.WARNING, "Sorry! something went to wrong while profile update.")
    context = {
        'form': form
    }
    template_name = 'agent/create_agent.html'
    return render(request, template_name, context)
