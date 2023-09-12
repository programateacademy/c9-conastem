from django.contrib import admin

# Register your models here.

from .models.Criterio import Criterio
from .models.Person_Responsable import PersonResponsable
from .models.Register import Register

# INFRAESTRUCTURA
from .models.INFRAESTRUCTURA.desarrollo_de_equipos_lideres import DesarrolloDeEquiposLideres
from .models.INFRAESTRUCTURA.planeacion_institucional import PlaneacionInstitucional
from .models.INFRAESTRUCTURA.ambiente_escolar import AmbienteEscolar
from .models.INFRAESTRUCTURA.recursos_tecnologicos import RecursosTecnologicos
from .models.INFRAESTRUCTURA.uso_de_informacion import UsoDeInformacion
from .models.INFRAESTRUCTURA.Equidad import Equidad

# CURRICULO
from .models.Curriculo.Inclusion_ingenieria_aula import Inclusion_ingenieria_aula
from .models.Curriculo.Desarrollo_ciudadania_digital import Desarrollo_ciudadania_digital

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .models.Formación_Instrucción_Evaluación.AprendizajeCentradoEstudiante import AprendizajeCentrado

# PERSONAL DOCENTE Y ADMINISTRATIVO

# ESCUELA COMUNIDAD Y PERTENENCIA
from .models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaCominudad
from .models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaCominudad
from .models.Escuela_Comunidad_y_Pertenencia.ConvivenciaEscolar import ConvivenciaEscolar
from .models.Escuela_Comunidad_y_Pertenencia.Sostenibilidad_EscuelaComunidadyPertenencia import Sostenibilidad_EscuelaComunidadyPertenencia


# ADMIN GENERALES
admin.site.register(Criterio)
admin.site.register(PersonResponsable)
admin.site.register(Register)


# ADMIN INFRAESTRUCTURA
admin.site.register(Equidad)


# ADMIN CURRICULO
admin.site.register(Inclusion_ingenieria_aula)
admin.site.register(Desarrollo_ciudadania_digital)


# ADMIN FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
admin.site.register(AprendizajeCentrado)


# ADMIN PERSONAL DOCENTE Y ADMINISTRATIVO


# ADMIN ESCUELA COMUNIDAD Y PERTENENCIA
admin.site.register(ConvivenciaEscolar)
admin.site.register(Sostenibilidad_EscuelaComunidadyPertenencia)
admin.site.register(CompromisodelaCominudad)
admin.site.register(RelacionesconlaCominudad)