from django.contrib import admin

# Register your models here.

from .models.INFRAESTRUCTURA.Equidad import Equidad 
from .models.Criterio import Criterio
from .models.Person_Responsable import PersonResponsable
from .models.Formación_Instrucción_Evaluación.AprendizajeCentradoEstudiante import AprendizajeCentrado

admin.site.register(Equidad)
admin.site.register(Criterio)
admin.site.register(PersonResponsable)
admin.site.register(AprendizajeCentrado)