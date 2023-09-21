from django import forms
# GENERALES
# GENERALES
from .models.Register import Register
from .models.Person_Responsable import PersonResponsable

# INFRAESTRUCTURA
from .models.Infraestructura import ambiente_escolar
from .models.Infraestructura import desarrollo_de_equipos_lideres
from .models.Infraestructura import equidad
from .models.Infraestructura import planeacion_institucional
from .models.Infraestructura import recursos_tecnologicos
from .models.Infraestructura import sostenibilidad
from .models.Infraestructura import uso_de_informacion

# CURRÍCULO

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante
from .models.Formacion_Instruccion_Evaluacion import ApredizajeRiguroso
from .models.Formacion_Instruccion_Evaluacion import EstrategiasFormativas
from .models.Formacion_Instruccion_Evaluacion import PlaneacionyCreaciondeActividades
from .models.Formacion_Instruccion_Evaluacion import AprendizajeExtendido
# PERSONAL DOCENTE Y ADMINISTRATIVO

# ESCUELA COMUNIDAD Y PERTENENCIA

# PERSONAL DOCENTE Y ADMINISTRATIVO

# ESCUELA COMUNIDAD Y PERTENENCIA
from .models.Escuela_Comunidad_y_Pertenencia import CompromisodelaComunidad
from .models.Escuela_Comunidad_y_Pertenencia import ConvivenciaEscolar
from .models.Escuela_Comunidad_y_Pertenencia import RelacionesconlaComunidad
from .models.Escuela_Comunidad_y_Pertenencia import Sostenibilidad_EscuelaComunidadyPertenencia

# WIDGETS
class DateInput(forms.DateInput):
    input_type = 'date'

class TextInput(forms.TextInput):
    input_type = 'text'

# FORMULARIOS GENERALES
class FormRegister(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ['id', 'created_date']

class FormPersonResponsable (forms.ModelForm):
    first_name = forms.CharField(required= True, widget= forms.TextInput(attrs={'placeholder' : 'Nombre'}))
    last_name = forms.CharField(required= True, widget= forms.TextInput(attrs={'placeholder' : 'Apellido'}))
    phone_number = forms.CharField(required= True, widget= forms.TextInput(attrs={'placeholder' : 'Número de teléfono'}))
    email = forms.EmailField(required= True, widget= forms.EmailInput(attrs={'placeholder' : 'Correo eléctronico'}))
    class Meta:
        model = PersonResponsable
        fields = ['first_name', 'last_name', 'phone_number', 'email']

# INFRAESTRUCTURA
class AmbienteEscolarForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = ambiente_escolar.AmbienteEscolar
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class DesarrolloEquiposLideresForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = desarrollo_de_equipos_lideres.DesarrolloDeEquiposLideres
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
        
class EquidadForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = equidad.Equidad
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
        
class PlaneacionInstitucionalForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = planeacion_institucional.PlaneacionInstitucional
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
        
class RecursosTecnologicosForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = recursos_tecnologicos.RecursosTecnologicos
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }        

class SostenibilidadForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = sostenibilidad.Sostenibilidad
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
        
class UsoDeInfoForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = uso_de_informacion.UsoDeInformacion
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
        
# CURRÍCULO


# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN

class Form_AprendizajeCentrado (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = AprendizajeCentradoEstudiante.AprendizajeCentrado
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
class Form_Aprendizajeriguroso (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = ApredizajeRiguroso.AprendizajeRiguroso
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
class Form_Planeacionycreaciondeactividades (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = PlaneacionyCreaciondeActividades.PlaneacionyCreaciondeActividades
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
class Form_Estrategiasformativas (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = EstrategiasFormativas.EstrategiasFormativas
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
class Form_Aprendizajeextendido (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = AprendizajeExtendido.AprendizajeExtendido
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }
# PERSONAL DOCENTE Y ADMINISTRATIVO


# ESCUELA COMUNIDAD Y PERTENENCIA

class Form_Compromisodelacomunidad (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = CompromisodelaComunidad.CompromisodelaComunidad
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_Convivenciaescolar (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = ConvivenciaEscolar.ConvivenciaEscolar
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_Relacionesconlacomunidad (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = RelacionesconlaComunidad.RelacionesconlaComunidad
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }


class Form_Sostenibilidadescuela (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Sostenibilidad_EscuelaComunidadyPertenencia.SostenibilidadEscuelaComunidadyPertenencia
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }