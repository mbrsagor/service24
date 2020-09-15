from django.views.generic import ListView, UpdateView, DetailView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse

from .models import User, Agent
from .forms import CreateAgentFrom
from service.models.order import Order


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProfileListView(ListView):
    model = User
    template_name = 'profile.html'
    context_object_name = 'order_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserListView(ListView):
    model = User
    paginate_by = 6
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
class UserDetailView(DetailView):
    template_name = 'profile.html'
    model = User


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UserDeleteView(View):

    def get(self, request, username):
        obj = User.objects.get(username=self.kwargs['username'])
        obj.delete()
        return redirect('/user/user-list/')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UpdateAgentProfile(SuccessMessageMixin, UpdateView):
    success_message = "Agent successfully updated!"
    template_name = 'agent/update_agent.html'
    model = Agent
    form_class = CreateAgentFrom

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(agent=self.request.user)

    def get_success_url(self):
        return reverse('update_agent_profile', kwargs={
            'pk': self.object.pk,
        })


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AgentProfile(ListView):
    model = Agent
    context_object_name = 'agent'
    template_name = 'agent/agent_profile.html'

    def get_queryset(self):
        return Agent.objects.get(agent=self.request.user)


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ListOfAgent(ListView):
    model = Agent
    paginate_by = 7
    context_object_name = 'agent_list'
    template_name = 'agent/agent_list.html'


class DeleteAgent(View):
    def get(self, request, id):
        obj = Agent.objects.get(id=id)
        obj.delete()
        return redirect('/user/agent-list/')
