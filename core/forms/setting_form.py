from django import forms
from core.models.setting import Setting


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = '__all__'

        widgets = {
            'logo_upload': forms.ImageField(attrs={'class': 'form-control'}),
            'favicon_upload': forms.ImageField(attrs={'class': 'form-control'}),
            'site_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'site_name'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'checkbox', 'id': 'is_active'}),
            'copy_write_text': forms.TextInput(attrs={'class': 'form-control', 'id': 'copy_write_text'})
        }
