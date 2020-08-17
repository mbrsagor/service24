from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect

from core.forms.auth.forms import CustomAuthenticationForm


class Login(LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = False
    template_name = 'auth/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)

        return super(LoginView, self).form_valid(form)


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')
