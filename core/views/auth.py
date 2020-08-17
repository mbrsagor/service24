from django.shortcuts import render
from django.views import View


class LoginView(View):

    def get(self, request):
        template_name = 'auth/login.html'
        return render(request, template_name)
