from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteViewfrom django.contrib.auth.decorators import login_requiredfrom django.utils.decorators import method_decoratorfrom django.contrib.messages.views import SuccessMessageMixinfrom django_filters.views import FilterViewfrom service.models.service import Servicefrom service.forms.service_form import ServiceFormfrom user.models import Agent, Userfrom service.forms.review_form import ReviewFormfrom service.filter.service_filter import ServiceFilter@method_decorator(login_required(login_url='/login/'), name='dispatch')class AddService(SuccessMessageMixin, CreateView):    template_name = 'services/add_service.html'    model = Service    form_class = ServiceForm    success_url = '/service/add-service/'    success_message = "Service has been successfully created!"    def form_valid(self, form):        obj = form.save(commit=False)        user = User.objects.get(id=self.request.user.id)        agent = Agent.objects.get(agent=user)        obj.owner = agent        obj.save()        return super(AddService, self).form_valid(form)@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceList(ListView):    template_name = 'services/service_list.html'    model = Service    context_object_name = 'service'    paginate_by = 7    def get_queryset(self):        if not self.request.user.is_superuser:            user = User.objects.get(id=self.request.user.id)            agent = Agent.objects.get(agent=user)            services = agent.service_owner.all()            return services        else:            services = self.model.objects.all()            return services@method_decorator(login_required(login_url='/login/'), name='dispatch')class AllService(ListView):    template_name = 'services/all_service.html'    model = Service    context_object_name = 'service'    paginate_by = 12@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceDetail(DetailView, CreateView):    template_name = 'services/service_details.html'    model = Service    context_object_name = 'service'    form_class = ReviewForm    success_url = '/service/all-service-list/'    def get_queryset(self):        if not self.request.user.is_superuser:            user = User.objects.get(id=self.request.user.id)            agent = Agent.objects.get(agent=user)            services = agent.service_owner.all()            return services        else:            services = self.model.objects.all()            return services@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceUpdate(SuccessMessageMixin, UpdateView):    template_name = 'services/add_service.html'    model = Service    form_class = ServiceForm    success_url = '/service/service-list/'    def form_valid(self, form):        obj = form.save(commit=False)        user = User.objects.get(id=self.request.user.id)        agent = Agent.objects.get(agent=user)        obj.owner = agent        obj.save()        return super(ServiceUpdate, self).form_valid(form)@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceDeleteView(DeleteView):    model = Service    success_url = '/service/service-list/'    template_name = 'services/service_confirm_delete.html'@method_decorator(login_required(login_url='/login/'), name='dispatch')class ServiceFilterView(FilterView, ListView):    template_name = 'services/service_filter.html'    model = Service    filter_class = ServiceFilter    context_object_name = 'service'    filterset_fields = ['service_name', 'price', 'category', 'location']