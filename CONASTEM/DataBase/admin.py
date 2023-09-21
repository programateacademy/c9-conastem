from django.contrib import admin

# Register your models here.


# GENERALES
from .models.Criterio import Criterio
from .models.Person_Responsable import PersonResponsable
from .models.Register import Register

# INFRAESTRUCTURA
from .models.Infraestructura.ambiente_escolar import AmbienteEscolar
from .models.Infraestructura.desarrollo_de_equipos_lideres import DesarrolloDeEquiposLideres
from .models.Infraestructura.Equidad import Equidad
from .models.Infraestructura.planeacion_institucional import PlaneacionInstitucional
from .models.Infraestructura.recursos_tecnologicos import RecursosTecnologicos
from .models.Infraestructura.sostenibilidad import Sostenibilidad
from .models.Infraestructura.uso_de_informacion import UsoDeInformacion

# CURRICULO
from .models.Curriculo.ConsideracionesSobreAreasYAsignaturas import ConsideracionesSobreAreasYAsignaturas
from .models.Curriculo.Inclusion_ingenieria_aula import InclusionIngenieriaAula
from .models.Curriculo.Desarrollo_ciudadania_digital import DesarrolloCiudadaniaDigital
from .models.Curriculo.Curriculo_progresivo import CurriculoProgresivo
from .models.Curriculo.Curriculo_propio import CurriculoPropio
from .models.Curriculo.Evaluacion_estudiantes import EvaluacionEstudiantes

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formacion_Instruccion_Evaluacion.AprendizajeCentradoEstudiante import AprendizajeCentrado
from .models.Formacion_Instruccion_Evaluacion.ApredizajeRiguroso import AprendizajeRiguroso
from .models.Formacion_Instruccion_Evaluacion.AprendizajeExtendido import AprendizajeExtendido
from .models.Formacion_Instruccion_Evaluacion.EstrategiasFormativas import EstrategiasFormativas
from .models.Formacion_Instruccion_Evaluacion.PlaneacionyCreaciondeActividades import PlaneacionyCreaciondeActividades
# from .models.Formacion_Instruccion_Evaluacion.EducacionSTEM import EducacionStemIntegrada
from .models.Formacion_Instruccion_Evaluacion.TecnologiaFormacionInstruccion import TecnologiaFormacion
from .models.Formacion_Instruccion_Evaluacion.EleccionCarrera import EleccionCarrera
from .models.Formacion_Instruccion_Evaluacion.Sostenibilidad import SostenibilidadFormacionInstruccion

# PERSONAL DOCENTE Y ADMINISTRATIVO
from .models.Personal_Docente_y_Administrativo.ProfesionalesEspecializadosEducacionSTEM import ProfesionalesEspecializadosEducacionSTEM
from .models.Personal_Docente_y_Administrativo.DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales import DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales
from .models.Personal_Docente_y_Administrativo.ApoyoPedagogico import ApoyoPedagogico
from .models.Personal_Docente_y_Administrativo.SostenibilidadDocenteAdministrativo import SostenibilidadDocenteAdministrativo

# ESCUELA COMUNIDAD Y PERTENENCIA
from .models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaComunidad
from .models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaComunidad
from .models.Escuela_Comunidad_y_Pertenencia.ConvivenciaEscolar import ConvivenciaEscolar
from .models.Escuela_Comunidad_y_Pertenencia.Sostenibilidad_EscuelaComunidadyPertenencia import SostenibilidadEscuelaComunidadyPertenencia


# ADMIN GENERALES
admin.site.register(Criterio)
admin.site.register(PersonResponsable)
admin.site.register(Register)


# ADMIN INFRAESTRUCTURA
admin.site.register(AmbienteEscolar)
admin.site.register(DesarrolloDeEquiposLideres)
admin.site.register(Equidad)
admin.site.register(PlaneacionInstitucional)
admin.site.register(RecursosTecnologicos)
admin.site.register(Sostenibilidad)
admin.site.register(UsoDeInformacion)

# ADMIN CURRICULO
admin.site.register(ConsideracionesSobreAreasYAsignaturas)
admin.site.register(InclusionIngenieriaAula)
admin.site.register(DesarrolloCiudadaniaDigital)
admin.site.register(CurriculoProgresivo)
admin.site.register(CurriculoPropio)
admin.site.register(EvaluacionEstudiantes)

# ADMIN FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
admin.site.register(AprendizajeCentrado)
admin.site.register(AprendizajeExtendido)
admin.site.register(AprendizajeRiguroso)
admin.site.register(PlaneacionyCreaciondeActividades)
admin.site.register(EstrategiasFormativas)
# admin.site.register(EducacionStemIntegrada)
admin.site.register(TecnologiaFormacion)
admin.site.register(EleccionCarrera)
admin.site.register(SostenibilidadFormacionInstruccion)


# ADMIN PERSONAL DOCENTE Y ADMINISTRATIVO
admin.site.register(DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales)
admin.site.register(SostenibilidadDocenteAdministrativo)
admin.site.register(ApoyoPedagogico)
admin.site.register(ProfesionalesEspecializadosEducacionSTEM)

# ADMIN ESCUELA COMUNIDAD Y PERTENENCIA
admin.site.register(ConvivenciaEscolar)
admin.site.register(SostenibilidadEscuelaComunidadyPertenencia)
admin.site.register(CompromisodelaComunidad)
admin.site.register(RelacionesconlaComunidad)
