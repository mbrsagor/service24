from django import formsfrom django.forms import TextInput, FileInput, NumberInput, URLInput, DateInputfrom .models import Agentclass CreateAgentFrom(forms.ModelForm):    class Meta:        model = Agent        fields = '__all__'        exclude = ['agent']        widgets = {            'company_name': TextInput(attrs={'class': 'form-control', 'id': 'company_name'}),            'nid_number': NumberInput(attrs={'class': 'form-control', 'id': 'nid_number'}),            'website': URLInput(attrs={'class': 'form-control', 'id': 'website'}),            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),            'age': DateInput(attrs={'class': 'form-control', 'id': 'age', 'placeholder': 'YYYY-MM-DD'}),            'contact_number': NumberInput(attrs={'class': 'form-control', 'id': 'contact_number'}),            'treat_lice': TextInput(attrs={'class': 'form-control', 'id': 'treat_lice'}),            'profile_picture': FileInput(attrs={'class': 'custom-file-input', 'id': 'imageUpload'}),        }