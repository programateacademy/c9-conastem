from django.views import generic
from ...models.INFRAESTRUCTURA.Equidad import Equidad

class EquidadView (generic.ListView):
    model= Equidad
    context_object_name= 'Equidad_SubCriterio'
    template_name= ''