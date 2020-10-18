from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from service.models.payment import Payment
from service.forms.payment_form import PaymentForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreatePayment(SuccessMessageMixin, CreateView):
    template_name = 'payment/add_payment.html'
    model = Payment
    form_class = PaymentForm
    success_url = '/service/payment/'
    success_message = "Payment has been successfully created!"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PaymentList(ListView):
    template_name = 'payment/payment_list.html'
    model = Payment
    context_object_name = 'payment'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class PaymentUpdate(UpdateView):
    template_name = 'payment/add_payment.html'
    model = Payment
    form_class = PaymentForm
    success_url = '/service/payment/'
