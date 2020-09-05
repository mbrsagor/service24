from django.views.generic import CreateView, ListViewfrom django.contrib.auth.decorators import login_requiredfrom django.utils.decorators import method_decoratorfrom django.contrib.messages.views import SuccessMessageMixinfrom service.models.service import Servicefrom service.forms.service_form import ServiceForm@method_decorator(login_required(login_url='/login/'), name='dispatch')class AddService(SuccessMessageMixin, CreateView):    template_name = 'services/add_service.html'    model = Service    form_class = ServiceForm    success_url = '/service/add-service/'    success_message = "Service has been successfully created!"@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceList(ListView):    template_name = 'services/service_list.html'    model = Service    context_object_name = 'service'