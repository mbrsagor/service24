from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from service.models.payment import Payment
from service.forms.payment_form import PaymentForm
from user.models import User, Agent


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreatePayment(SuccessMessageMixin, CreateView):
    template_name = 'payment/add_payment.html'
    model = Payment
    form_class = PaymentForm
    success_url = '/service/payment/'
    success_message = "Payment has been successfully created!"

    def form_valid(self, form):
        obj = form.save(commit=False)
        user = User.objects.get(id=self.request.user.id)
        agent = Agent.objects.get(agent_id=user)
        obj.agent = agent
        obj.save()
        return super(CreatePayment, self).form_valid(form)
