from django.views.generic import CreateView, ListView, DetailViewfrom django.contrib.auth.decorators import login_requiredfrom django.utils.decorators import method_decoratorfrom django.contrib.messages.views import SuccessMessageMixinfrom django.shortcuts import redirectfrom django.views import Viewfrom service.models.service import Servicefrom service.forms.service_form import ServiceFormfrom user.models import Agent, User@method_decorator(login_required(login_url='/login/'), name='dispatch')class AddService(SuccessMessageMixin, CreateView):    template_name = 'services/add_service.html'    model = Service    form_class = ServiceForm    success_url = '/service/add-service/'    success_message = "Service has been successfully created!"@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceList(ListView):    template_name = 'services/service_list.html'    model = Service    context_object_name = 'service'    def get_queryset(self):        if not self.request.user.is_superuser:            user = User.objects.get(id=self.request.user.id)            agent = Agent.objects.get(agent=user)            services = agent.service_owner.all()            return services        else:            services = self.model.objects.all()            return services@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceDetail(DetailView):    template_name = 'services/service_details.html'    model = Service    context_object_name = 'service'    def get_queryset(self):        if not self.request.user.is_superuser:            user = User.objects.get(id=self.request.user.id)            agent = Agent.objects.get(agent=user)            services = agent.service_owner.all()            return services        else:            services = self.model.objects.all()            return services@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceDeleteView(View):    def get(self, request, id):        obj = Service.objects.get(id=self.kwargs['id'])        obj.delete()        return redirect('/service/service-list/')