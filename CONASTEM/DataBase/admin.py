from django.contrib import admin

# GENERALES
from .models.Criterio import Criterio
from .models.Person_Responsable import PersonResponsable
from .models.Register import Register

# INFRAESTRUCTURA
from .models.Infraestructura.Equidad import Equidad 

# CURRICULO
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

from .models.Formacion_Instruccion_Evaluacion.TecnologiaFormacionInstruccion import TecnologiaFormacion
from .models.Formacion_Instruccion_Evaluacion.EleccionCarrera import EleccionCarrera
from .models.Formacion_Instruccion_Evaluacion.Sostenibilidad import SostenibilidadFormacionInstruccion

# PERSONAL DOCENTE Y ADMINISTRATIVO

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
admin.site.register(Equidad)


# ADMIN CURRICULO
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

admin.site.register(TecnologiaFormacion)
admin.site.register(EleccionCarrera)
admin.site.register(SostenibilidadFormacionInstruccion)

# ADMIN PERSONAL DOCENTE Y ADMINISTRATIVO


# ADMIN ESCUELA COMUNIDAD Y PERTENENCIA
admin.site.register(ConvivenciaEscolar)
admin.site.register(SostenibilidadEscuelaComunidadyPertenencia)
admin.site.register(CompromisodelaComunidad)
admin.site.register(RelacionesconlaComunidad)