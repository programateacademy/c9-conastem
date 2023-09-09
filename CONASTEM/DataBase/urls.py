from django.urls import path
from .views import views
from .views import EscuelaComunidadYPertenencia


urlpatterns= [
<<<<<<< HEAD
    path('', views.CriterioList.as_view(), name= 'criterio_list'),
=======
    path('', views.index, name= 'index'),
]

urlpatterns += [
    path("Escuelacomunidadypertenencia",EscuelaComunidadYPertenencia.CompromisodelaComunidadListView.as_view(),name="Escuelacomunidadypertenencia"),
>>>>>>> 5b9c164413a0b8f059e2c738262412d5491e3f7a
]