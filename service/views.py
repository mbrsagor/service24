from django.shortcuts import render
from django.views import View


class Dashboard(View):
    def get(self, request):
        template_name = 'dashboard.html'
        return render(request, template_name)
