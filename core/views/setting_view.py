from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from core.forms.setting_form import SettingForm
from core.models.setting import Setting


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ApplicationSetting(SuccessMessageMixin, generic.CreateView, generic.ListView):
    model = Setting
    form_class = SettingForm
    success_message = "Application setting updated successfully!"
