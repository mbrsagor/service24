from django.views.generic.base import TemplateViewclass Homepage(TemplateView):    template_name = 'frontend/homepage.html'    def dispatch(self, *args, **kwargs):        return super(Homepage, self).dispatch(*args, **kwargs)