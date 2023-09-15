from django import forms
from .models.Register import Register
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante

#Infraestructura model

from .models.Infraestructura import ambiente_escolar
from .models.Infraestructura import desarrollo_de_equipos_lideres
from .models.Infraestructura import equidad
from .models.Infraestructura import planeacion_institucional
from .models.Infraestructura import recursos_tecnologicos
from .models.Infraestructura import sostenibilidad
from .models.Infraestructura import uso_de_informacion   
        
class FormRegister(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ['id', 'created_date']
        
class Form_Criterio_3 (forms.ModelForm):
    class Meta:
        model = AprendizajeCentradoEstudiante.AprendizajeCentrado
        fields = ['criterio', 'numeral', 'subnumeral', 'priority', 'person_responsable', 'dep_responsable', 'track_year', 'track_date', 
                'internal_auditory_date', 'internal_auditory_obs', 'external_auditory_date', 'external_auditory_obs']
        exclude = ['created_at', 'updated_at']