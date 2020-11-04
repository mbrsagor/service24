from django import formsfrom django.forms import TextInput, FileInput, NumberInput, URLInput, DateInputfrom .models import Agent, Profileclass CreateAgentFrom(forms.ModelForm):    class Meta:        model = Agent        fields = '__all__'        exclude = ['agent_id', 'agent']        widgets = {            'company_name': TextInput(attrs={'class': 'form-control', 'id': 'company_name'}),            'nid_number': NumberInput(attrs={'class': 'form-control', 'id': 'nid_number'}),            'website': URLInput(attrs={'class': 'form-control', 'id': 'website'}),            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),            'age': DateInput(attrs={'class': 'form-control', 'id': 'age',                                    'type': 'date'}),            'contact_number': NumberInput(attrs={'class': 'form-control', 'id': 'contact_number'}),            'treat_lice': TextInput(attrs={'class': 'form-control', 'id': 'treat_lice'}),            'profile_picture': FileInput(attrs={'class': 'custom-file-input', 'id': 'imageUpload'}),        }class ProfileForm(forms.ModelForm):    class Meta:        model = Profile        fields = '__all__'        exclude = ['user', 'user_id']        widgets = {            'first_name': TextInput(attrs={'class': 'form-control', 'id': 'first_name'}),            'last_name': TextInput(attrs={'class': 'form-control', 'id': 'last_name'}),            'address': TextInput(attrs={'class': 'form-control', 'id': 'address'}),            'profession': TextInput(attrs={'class': 'form-control', 'id': 'profession'}),            'age': NumberInput(attrs={'class': 'form-control', 'id': 'age'}),            'profile_picture': FileInput(attrs={'class': 'form-control', 'id': 'imageUpload'}),        }