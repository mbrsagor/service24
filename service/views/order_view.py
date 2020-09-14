from django.views.generic import CreateView, ListViewfrom django.contrib.auth.decorators import login_requiredfrom django.utils.decorators import method_decoratorfrom service.models.order import Orderfrom service.forms.order_form import OrderForm@method_decorator(login_required(login_url='/login/'), name='dispatch')class OrderList(ListView):    template_name = 'order/order_list.html'    model = Order    context_object_name = 'order_list'    def get_queryset(self):        if not self.request.user.is_superuser:            _order = self.model.objects.filter(user=self.request.user)        else:            _order = self.model.objects.all()        return _order@method_decorator(login_required(login_url='/login/'), name='dispatch')class CreateOrder(CreateView):    template_name = 'order/add_order.html'    model = Order    form_class = OrderForm    success_url = '/service/new-order/'    success_message = "Your order has been successfully done!"    def form_valid(self, form):        obj = form.save(commit=False)        obj.user = self.request.user        obj.save()        return super(CreateOrder, self).form_valid(form)