from django.urls import path
from .views import views
from .views import EscuelaComunidadYPertenencia
from ...models.Curriculo.Inclusion_ingenieria_aula import Inclusion_ingenieria_aula

from .views.Curriculo.Inclusion_ingenieria_aula import Inclusion_ingenieria_aula
# from .models.Curriculo.Inclusion_ingenieria_aula import Inclusion_ingenieria_aula
urlpatterns= [
    path('', views.index, name= 'index'),
]

urlpatterns += [
    path("Escuelacomunidadypertenencia",EscuelaComunidadYPertenencia.CompromisodelaComunidadListView.as_view(),name="Escuelacomunidadypertenencia"),
# CURRICULO
    # 2.2 Inclusion_ingenieria_aula
    path('lista_inclusiones/', Inclusion_ingenieria_aula.iInclusionIngenieriaAulaListView.as_view(), name='lista_inclusiones'),
    path('detalle_inclusion/<int:pk>/', Inclusion_ingenieria_aula.InclusionIngenieriaAulaListView.as_view(), name='detalle_inclusion'),
    path('crear_inclusion/', Inclusion_ingenieria_aula.InclusionIngenieriaAulaListView.as_view(), name='crear_inclusion'),
    path('editar_inclusion/<int:pk>/', Inclusion_ingenieria_aula.InclusionIngenieriaAulaListView.as_view(), name='editar_inclusion'),
    path('eliminar_inclusion/<int:pk>/', Inclusion_ingenieria_aula.InclusionIngenieriaAulaListView.as_view(), name='eliminar_inclusion'),
]
