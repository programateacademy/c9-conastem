from django.contrib import admin

# Register your models here.

from .models.INFRAESTRUCTURA.Equidad import Equidad 
from .models.Criterio import Criterio
from .models.Auditory import Auditory
from .models.Person_Responsable import PersonResponsable

admin.site.register(Equidad)
admin.site.register(Criterio)
admin.site.register(Auditory)
admin.site.register(PersonResponsable)