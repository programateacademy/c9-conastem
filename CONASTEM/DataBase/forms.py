from django import forms
from .models.Register import Register


class FormRegister(forms.ModelForm):

    class Meta:
        model = Register
        exclude = ['id', 'created_date']


