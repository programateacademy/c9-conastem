from django.contrib import admin

# Register your models here.

# from .models.Infraestructura.Equidad import Equidad 
from .models.Criterio import Criterio
from .models.Person_Responsable import PersonResponsable
from .models.Formación_Instrucción_Evaluación.AprendizajeCentradoEstudiante import AprendizajeCentrado
from .models.Escuela_Comunidad_y_Pertenencia.CompromisodelaComunidad import CompromisodelaCominudad
from .models.Escuela_Comunidad_y_Pertenencia.RelacionesconlaComunidad import RelacionesconlaCominudad
# admin.site.register(Equidad)
admin.site.register(Criterio)
admin.site.register(PersonResponsable)
admin.site.register(AprendizajeCentrado)
admin.site.register(CompromisodelaCominudad)
admin.site.register(RelacionesconlaCominudad)