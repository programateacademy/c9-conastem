from django import forms

# GENERALES
from .models.Register import Register
from .models.Person_Responsable import PersonResponsable

# INFRAESTRUCTURA
from .models.Infraestructura import ambiente_escolar
from .models.Infraestructura import desarrollo_de_equipos_lideres
from .models.Infraestructura import equidad
from .models.Infraestructura import planeacion_institucional
from .models.Infraestructura import recursos_tecnologicos
from .models.Infraestructura import sostenibilidad_infraestructura
from .models.Infraestructura import uso_de_informacion

# CURRÍCULO
from .models.Curriculo import ConsideracionesSobreAreasYAsignaturas
from .models.Curriculo import IntegracionCurricular
from .models.Curriculo import DesarrolloHabilidadesSigloXXI
from .models.Curriculo import SostenibilidadCurriculo
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
from .models.Formacion_Instruccion_Evaluacion import SostenibilidadFormacionInstruccion
from .models.Formacion_Instruccion_Evaluacion import ApredizajeRiguroso
from .models.Formacion_Instruccion_Evaluacion import EstrategiasFormativas
from .models.Formacion_Instruccion_Evaluacion import PlaneacionyCreaciondeActividades
from .models.Formacion_Instruccion_Evaluacion import AprendizajeExtendido

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
    # FORMULARIO DE REGISTRO DE INSTITUCIONES
class FormRegister(forms.ModelForm):
    institution_name = forms.CharField(label='', required= True, widget= forms.TextInput(attrs={'placeholder': 'Nombre institución'}))
    nit = forms.IntegerField(label='', required= False, widget= forms.NumberInput(attrs={'placeholder' : 'NIT'}) )
    adress = forms.CharField(label='', required= True, widget= forms.TextInput(attrs={'placeholder' : 'Dirección'}))
    institution_responsable = forms.CharField(label='', required= True, widget= forms.TextInput(attrs={'placeholder' : 'Responsable'}))
    phone = forms.IntegerField(label='', required= True, widget= forms.NumberInput(attrs={'placeholder' : 'Teléfono'}))
    email = forms.EmailField(label='', required= True, widget= forms.EmailInput(attrs={'placeholder' : 'Correo electrónico'}))
    year = forms.IntegerField(label='', required= True, widget= forms.NumberInput(attrs={'placeholder' : 'Año de inscripción'}))
    class Meta:
        model = Register
        exclude = ['id', 'created_date']

    # FORMULARIO DE REGISTRO DE PERSONA RESPONSABLE
class FormPersonResponsable (forms.ModelForm):
    first_name = forms.CharField(label='', required= True, widget= forms.TextInput(attrs={'placeholder' : 'Nombre'}))
    last_name = forms.CharField(label='', required= True, widget= forms.TextInput(attrs={'placeholder' : 'Apellido'}))
    phone_number = forms.CharField(label='', required= True, widget= forms.TextInput(attrs={'placeholder' : 'Número de teléfono'}))
    email = forms.EmailField(label='', required= True, widget= forms.EmailInput(attrs={'placeholder' : 'Correo eléctronico'}))
    class Meta:
        model = PersonResponsable
        fields = ['first_name', 'last_name', 'phone_number', 'email']

# INFRAESTRUCTURA

# 1.1 DESARROLLO DE EQUIPOS LÍDERES
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

# 1.2 PLANEACIÓN INSTITUCIONAL
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

# 1.3 AMBIENTE ESCOLAR
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

# 1.4 RECURSOS TECNOLÓGICOS
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

# 1.5 USO DE LA INFORMACIÓN (DATOS)
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

# 1.6 EQUIDAD
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

# 1.7 SOSTENIBILIDAD - INFRAESTRUCTURA
class SostenibilidadForm (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = sostenibilidad_infraestructura.Sostenibilidad
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        } 


# CURRÍCULO

# 2.1 CONSIDERACIONES SOBRE LAS ÁREAS Y LAS ASIGNATURAS
class Form_ConsideracionesSobreAreasYAsignaturas(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = ConsideracionesSobreAreasYAsignaturas.ConsideracionesSobreAreasYAsignaturas
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

# 2.2 INCLUSIÓN DE LA INGENIERÍA EN EL AULA
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

# 2.3 DESARROLLO DE UNA CIUDADANÍA DIGITAL
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

# 2.4 INTEGRACIÓN CURRICULAR
class Form_IntegracionCurricular(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = IntegracionCurricular.IntegracionCurricular
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

# 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
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

# 2.6 CURRÍCULO PROPIO
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

# 2.7 DESARROLLO DE LAS HABILIDADES DEL SIGLO XXI
class Form_DesarrolloHabilidadesSigloXXI(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = DesarrolloHabilidadesSigloXXI.DesarrolloHabilidadesSigloXXI
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }

# 2.8 EVALUACIÓN DE LOS ESTUDIANTES
class Form_EvaluacionEstudiantes(forms.ModelForm):
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

# 2.9 SOSTENIBILIDAD - CURRÍCULO
class Form_SostenibilidadCurriculo(forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = SostenibilidadCurriculo.SostenibilidadCurriculo
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }


# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN

# 3.1 APRENDIZAJE CENTRADO EN EL ESTUDIANTE
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

# 3.2 APRENDIZAJE RIGUROSO
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

# 3.3 PLANEACIÓN Y CREACIÓN DE ACTIVIDADES
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

# 3.4 EDUCACIÓN STEM INTEGRADA
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

# 3.5 TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN
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

# 3.6 ESTRATEGIAS FORMATIVAS
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

# 3.7 ELECCIÓN DE CARRERA
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

# 3.8 APRENDIZAJE EXTENDIDO
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

# 3.9 SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN
class Form_SostenibilidadFormacion (forms.ModelForm):
    dep_responsable = forms.CharField(label= 'Departamento responsable', required= True, widget= forms.TextInput(attrs={'placeholder': 'Dirección'}))
    class Meta:
        model = SostenibilidadFormacionInstruccion.SostenibilidadFormacionInstruccion
        exclude = ['created_at', 'updated_at','codigo']
        widgets = {
            'priority' : TextInput(attrs={'class' : 'campo-formulario'}),
            'track_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'internal_auditory_date' : DateInput(attrs={'class': 'campo-formulario'}),
            'external_auditory_date' : DateInput(attrs={'class': 'campo-formulario'})
        }


# PERSONAL DOCENTE Y ADMINISTRATIVO


# ESCUELA COMUNIDAD Y PERTENENCIA

# 5.1 COMPROMISO DE LA COMUNIDAD
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

# 5.2 RELACIONES CON LA COMUNIDAD
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

# 5.3 CONVIVENCIA ESCOLAR
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

# 5.4 SOSTENIBILIDAD - ESCUELA, COMUNIDAD Y PERTENENCIA
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