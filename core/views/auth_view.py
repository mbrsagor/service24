from django.views import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import resolve_url
from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from core.forms.auth.forms import CustomAuthenticationForm
from core.forms.auth.registrationForm import CustomUserCreationForm
from user.models import User


class Login(LoginView):
    authentication_form = CustomAuthenticationForm
    form_class = CustomAuthenticationForm
    redirect_authenticated_user = False
    template_name = 'auth/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/dashboard/')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(Login, self).form_valid(form)


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/login/')


class SingUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/signup.html'


def forgot_password(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            if not User.objects.filter(username=username).first():
                messages.success(request, "Not user found with this username.")
                return redirect('/')
            user_obj = User.objects.get(username=username)
            print(user_obj)
    except Exception as ex:
        print(ex)
    template_name = 'auth/forgot_password.html'
    return render(request, template_name)
