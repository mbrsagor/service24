from django.forms import ModelForm
from django.forms.widgets import TextInput, FileInput

from service.models.payment import Payment


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

        widgets = {
            'name': TextInput(
                attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter payment name'}),
            'logo': FileInput(attrs={'class': 'custom-file-input', 'id': 'imageUpload'}),
        }
