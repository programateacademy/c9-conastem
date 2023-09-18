from django import forms
from .models.Register import Register
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante
from .models.Escuela_Comunidad_y_Pertenencia import CompromisodelaComunidad


class FormRegister(forms.ModelForm):

    class Meta:
        model = Register
        exclude = ['id', 'created_date']

class Form_Criterio_3 (forms.ModelForm):
    class Meta:
        model = AprendizajeCentradoEstudiante.AprendizajeCentrado
        exclude = ['created_at', 'updated_at']

class Form_Compromisodelacomunidad (forms.ModelForm):
    class Meta:
        model = CompromisodelaComunidad.CompromisodelaComunidad
        exclude = ['created_at', 'updated_at']

