from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from service.models.payment import Payment
from service.forms.payment_form import PaymentForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PaymentCreateList(SuccessMessageMixin, CreateView, ListView):
    template_name = 'payment/payment_list.html'
    model = Payment
    form_class = PaymentForm
    success_url = '/service/payment/'
    success_message = "Payment successfully created!"
    paginate_by = 6
    context_object_name = 'payment'

    def get_context_data(self, **kwargs):
        return dict(
            super(PaymentCreateList, self).get_context_data(**kwargs),
            payment=self.model.objects.all().order_by('-id')
        )


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PaymentUpdate(UpdateView):
    template_name = 'payment/payment_list.html'
    model = Payment
    form_class = PaymentForm
    success_url = '/service/payment/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PaymentDelete(DeleteView):
    template_name = 'payment/payment_confirm_delete.html'
    model = Payment
    success_url = '/service/payment/'
