from django import forms
from .models.Register import Register


class FormRegister(forms.ModelForm):

    class Meta:
        model = Register
        fields = ('institution_name', 'nit', 'adress', 'institution_responsable', 'phone', 'email', 'model')
    


