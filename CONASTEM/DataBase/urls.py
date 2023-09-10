from django.urls import path
from .views import views
from .views import EscuelaComunidadYPertenencia
from .views import Curriculo


urlpatterns= [
    path('', views.index, name= 'index'),
]

urlpatterns += [
    path("Escuelacomunidadypertenencia",EscuelaComunidadYPertenencia.CompromisodelaComunidadListView.as_view(),name="Escuelacomunidadypertenencia"),
    path("Curriculo",Curriculo.Inclusion_ingenieria_aula_ListView.as_view(),name="Curriculo")
]
