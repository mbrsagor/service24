from django.forms import ModelForm, TextInput, CheckboxInput, ImageField
from core.models.setting import Setting


class SettingForm(ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'

        widgets = {
            'logo_upload': ImageField(attrs={'class': 'form-control'}),
            'favicon_upload': ImageField(attrs={'class': 'form-control'}),
            'site_name': TextInput(attrs={'class': 'form-control', 'id': 'site_name'}),
            'is_active': CheckboxInput(attrs={'class': 'checkbox', 'id': 'is_active'}),
            'copy_write_text': TextInput(attrs={'class': 'form-control', 'id': 'copy_write_text'})
        }
