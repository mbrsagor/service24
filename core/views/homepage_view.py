from django.views.generic.base import TemplateViewfrom service.models.service import Serviceclass Homepage(TemplateView):    template_name = 'frontend/homepage.html'    def dispatch(self, *args, **kwargs):        return super(Homepage, self).dispatch(*args, **kwargs)    def get_context_data(self, **kwargs):        context = super().get_context_data(**kwargs)        context['latest_service'] = Service.objects.all().order_by('-id')[:5]        return context