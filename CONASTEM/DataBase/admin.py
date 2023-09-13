from django.contrib import admin

# Register your models here.

# from .models.Infraestructura.Equidad import Equidad 
from .models.Criterio import Criterio
from .models.Person_Responsable import PersonResponsable
from .models.Formación_Instrucción_Evaluación.AprendizajeCentradoEstudiante import AprendizajeCentrado
# Escuela Comunidad y Pertenencia
from .models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaComunidad
from .models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaCominudad
from .models.Escuela_Comunidad_y_Pertenencia.ConvivenciaEscolar import ConvivenciaEscolar
from .models.Escuela_Comunidad_y_Pertenencia.Sostenibilidad_EscuelaComunidadyPertenencia import SostenibilidadEscuelaComunidadyPertenencia
# Currículo
from .models.Curriculo.Inclusion_ingenieria_aula import Inclusion_ingenieria_aula
from .models.Curriculo.Desarrollo_ciudadania_digital import Desarrollo_ciudadania_digital

# admin.site.register(Equidad)
admin.site.register(ConvivenciaEscolar)
admin.site.register(SostenibilidadEscuelaComunidadyPertenencia)
admin.site.register(Criterio)
admin.site.register(PersonResponsable)
admin.site.register(AprendizajeCentrado)
admin.site.register(CompromisodelaComunidad)
admin.site.register(RelacionesconlaCominudad)
# admin curriculo
admin.site.register(Inclusion_ingenieria_aula)
admin.site.register(Desarrollo_ciudadania_digital)
