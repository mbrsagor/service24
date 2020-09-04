from django.views.generic import ListView, UpdateView
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView

from .models import User, Agent
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


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UpdateAgentProfile(SuccessMessageMixin, UpdateView):
    success_message = "Agent successfully updated!"
    template_name = 'agent/update_agent.html'
    success_url = f'/user/update-agent-profile/{id}'
    model = Agent
    form_class = CreateAgentFrom

    # def get_object(self, **kwargs):
    #     username = self.kwargs.get("username")
    #     if username is None:
    #         raise redirect('/login/')
    #     return get_object_or_404(Agent, user__username__iexact=username)


class AgentProfile(TemplateView):
    template_name = 'agent/agent_profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AgentProfile, self).dispatch(*args, **kwargs)
