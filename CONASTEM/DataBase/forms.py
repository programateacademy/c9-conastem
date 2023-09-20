from django import forms
# GENERALES
# GENERALES
from .models.Register import Register
from .models.Person_Responsable import PersonResponsable

# INFRAESTRUCTURA

# CURRÍCULO
from .models.Curriculo import Inclusion_ingenieria_aula
from .models.Curriculo import Desarrollo_ciudadania_digital
from .models.Curriculo import Curriculo_progresivo
from .models.Curriculo import Curriculo_propio
from .models.Curriculo import Evaluacion_estudiantes

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante
from .models.Formacion_Instruccion_Evaluacion import EducacionSTEM
from .models.Formacion_Instruccion_Evaluacion import TecnologiaFormacionInstruccion
from .models.Formacion_Instruccion_Evaluacion import EleccionCarrera
from .models.Formacion_Instruccion_Evaluacion import Sostenibilidad

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


# CURRÍCULO

class Form_IngenieriaAula(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Inclusion_ingenieria_aula.InclusionIngenieriaAula
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_DesarrolloCiudadania(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Desarrollo_ciudadania_digital.DesarrolloCiudadaniaDigital
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_CurriculoProgresivo(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Curriculo_progresivo.CurriculoProgresivo
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_CurriculoPropio(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Curriculo_propio.CurriculoPropio
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_EvaluacionEstudiantes(forms.Form):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Evaluacion_estudiantes.EvaluacionEstudiantes
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }


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

class Form_EducacionSTEM (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = EducacionSTEM.EducacionSTEMIntegrada
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_TecFormacionInstruccion (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = TecnologiaFormacionInstruccion.TecnologiaFormacion
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_EleccionCarrera (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = EleccionCarrera.EleccionCarrera
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_SostenibilidadFormacion (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = Sostenibilidad.SostenibilidadFormacionInstruccion
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
    class Meta:
        model = CompromisodelaComunidad.CompromisodelaComunidad
        exclude = ['created_at', 'updated_at','codigo']

class Form_Convivenciaescolar (forms.ModelForm):
    class Meta:
        model = ConvivenciaEscolar.ConvivenciaEscolar
        exclude = ['created_at', 'updated_at','codigo']

class Form_Relacionesconlacomunidad (forms.ModelForm):
    class Meta:
        model = RelacionesconlaComunidad.RelacionesconlaComunidad
        exclude = ['created_at', 'updated_at','codigo']


class Form_Sostenibilidadescuela (forms.ModelForm):
    class Meta:
        model = Sostenibilidad_EscuelaComunidadyPertenencia.SostenibilidadEscuelaComunidadyPertenencia
        exclude = ['created_at', 'updated_at','codigo']