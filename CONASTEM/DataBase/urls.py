from django.urls import path
from .views import views
from .views import EscuelaComunidadYPertenencia


urlpatterns= [
    path('', views.index, name= 'index'),
]

urlpatterns += [
    path("Escuelacomunidadypertenencia",EscuelaComunidadYPertenencia.CompromisodelaComunidadListView.as_view(),name="Escuelacomunidadypertenencia"),
]