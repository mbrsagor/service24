from django.conf import settings
from django.views import generic
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import user_passes_test

from user.forms import CreateAgentFrom

"""
Title: Create agent from admin.
Desc: Admin can create any kind of agents from here.
"""


@method_decorator(user_passes_test(lambda user: user.is_superuser or user.is_staff), name='dispatch')
class CreateUserView(SuccessMessageMixin, generic.CreateView):
    """
    Name: Create agent.
    Desc: Admin will create user from the system.
    """
    form_class = CreateAgentFrom
    success_url = reverse_lazy('create_user')
    success_message = 'The agent has been created successfully.'
    template_name = 'agent/create_agent.html'

    def form_valid(self, form):
        cd = form.cleaned_data
        email_to = cd['email']
        subject = "{0} Login credentials ".format(
            cd['email'])
        mes = "Welcome to BD service24 new member! Please check below your login credentials for login in your account."
        message = f"{mes}\n\nPhone Number: {cd['phone_number']}\nPassword: {cd['password1']}"
        send_mail(subject, message, settings.EMAIL_HOST, [email_to, ])
        return super().form_valid(form)
