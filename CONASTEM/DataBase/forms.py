from django import forms
# GENERALES
# GENERALES
from .models.Register import Register
from .models.Person_Responsable import PersonResponsable

# INFRAESTRUCTURA

# CURRÍCULO

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante

# PERSONAL DOCENTE Y ADMINISTRATIVO
from .models.Personal_Docente_y_Administrativo import ProfesionalesEspecializadosEducacionSTEM
from .models.Personal_Docente_y_Administrativo import DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
from .models.Personal_Docente_y_Administrativo import ApoyoPedagogico
from .models.Personal_Docente_y_Administrativo import SostenibilidadDocenteAdministrativo

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

# PERSONAL DOCENTE Y ADMINISTRATIVO
class Form_ApoyoPedagogico (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = ApoyoPedagogico.ApoyoPedagogico
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales.DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

class Form_ProfesionalesEspecializadosEducacionSTEM (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = ProfesionalesEspecializadosEducacionSTEM.ProfesionalesEspecializadosEducacionSTEM
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }


class Form_SostenibilidadDocenteAdministrativo (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = SostenibilidadDocenteAdministrativo.SostenibilidadDocenteAdministrativo
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

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