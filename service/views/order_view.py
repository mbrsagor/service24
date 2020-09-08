from django.views.generic import ListViewfrom django.contrib.auth.decorators import login_requiredfrom django.utils.decorators import method_decoratorfrom service.models.order import Order@method_decorator(login_required(login_url='/login/'), name='dispatch')class OrderList(ListView):    template_name = 'order/order_list.html'    model = Order    context_object_name = 'order_list'    def get_queryset(self):        if not self.request.user.is_superuser:            _order = self.model.objects.filter(user=self.request.user)        else:            _order = self.model.objects.all()        return _order