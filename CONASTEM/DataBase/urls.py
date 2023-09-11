from django.urls import path

from .views import views
from .views.Curriculo.Inclusion_ingenieria_aula import InclusionIngenieriaAulaListView
from .views.Curriculo.Desarrollo_ciudadania_digital import DesarrolloCiudadaniaDigitalListView
from .views.EscuelaComunidadYPertenencia import CompromisodelaComunidadListView

urlpatterns= [
    path('', views.CriterioList.as_view(), name= 'criterio_list'),
]
urlpatterns += [
    path("Escuelacomunidadypertenencia",EscuelaComunidadYPertenencia.EscuelaComunidadyPertenenciaListView.as_view(),name="Escuelacomunidadypertenencia"),

    path('inclusion_ingenieria_aula/', InclusionIngenieriaAulaListView.as_view(), name='inclusion_ingenieria_aula_list'),

    # 2.3 Desarrollo ciudadania digital
    path('desarrollo-ciudadania-digital/', DesarrolloCiudadaniaDigitalListView.as_view(), name='desarrollo_ciudadania_digital_list'),
]


