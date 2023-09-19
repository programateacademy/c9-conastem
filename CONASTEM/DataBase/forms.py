from django import forms
# GENERALES
from .models.Register import Register

# INFRAESTRUCTURA

# CURRÍCULO

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante

# PERSONAL DOCENTE Y ADMINISTRATIVO

# ESCUELA COMUNIDAD Y PERTENENCIA
from .models.Escuela_Comunidad_y_Pertenencia import CompromisodelaComunidad
from .models.Escuela_Comunidad_y_Pertenencia import ConvivenciaEscolar
from .models.Escuela_Comunidad_y_Pertenencia import RelacionesconlaComunidad
from .models.Escuela_Comunidad_y_Pertenencia import Sostenibilidad_EscuelaComunidadyPertenencia

# FORMULARIOS GENERALES
class FormRegister(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ['id', 'created_date']


# INFRAESTRUCTURA


# CURRÍCULO


# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN

class Form_AprendizajeCentrado (forms.ModelForm):
    class Meta:
        model = AprendizajeCentradoEstudiante.AprendizajeCentrado
        exclude = ['created_at', 'updated_at']

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