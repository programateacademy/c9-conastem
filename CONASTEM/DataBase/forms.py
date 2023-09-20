from django import forms
# GENERALES
from .models.Register import Register

# INFRAESTRUCTURA

# CURRÍCULO
from .models.Curriculo import ConsideracionesSobreAreasYAsignaturas
from .models.Curriculo import IntegracionCurricular
from .models.Curriculo import DesarrolloHabilidadesSigloXXI
from .models.Curriculo import SostenibilidadCurriculo

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formacion_Instruccion_Evaluacion import AprendizajeCentradoEstudiante

# PERSONAL DOCENTE Y ADMINISTRATIVO

# ESCUELA COMUNIDAD Y PERTENENCIA
from .models.Escuela_Comunidad_y_Pertenencia import CompromisodelaComunidad
from .models.Escuela_Comunidad_y_Pertenencia import ConvivenciaEscolar

# FORMULARIOS GENERALES
class FormRegister(forms.ModelForm):
    class Meta:
        model = Register
        exclude = ['id', 'created_date']


# INFRAESTRUCTURA


# CURRÍCULO
class Form_ConsideracionesSobreAreasYAsignaturas(forms.ModelForm):
    class Meta:
        model = ConsideracionesSobreAreasYAsignaturas.ConsideracionesSobreAreasYAsignaturas
        exclude = ['created_at', 'updated_at','codigo']

class Form_IntegracionCurricular(forms.ModelForm):
    class Meta:
        model = IntegracionCurricular.Integracioncurricular
        exclude = ['created_at', 'updated_at','codigo']

class Form_DesarrolloHabilidadesSigloXXI(forms.ModelForm):
    class Meta:
        model = DesarrolloHabilidadesSigloXXI.DesarroloHabilidadesSigloXXI
        exclude = ['created_at', 'updated_at','codigo']

class Form_SostenibilidadCurriculo(forms.Form):
    class Meta:
        model = SostenibilidadCurriculo.SostenibilidadCurriculo
        exclude = ['created_at', 'updated_at','codigo']



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