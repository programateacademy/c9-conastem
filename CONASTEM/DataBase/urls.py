from django.urls import path
# from .views import *
from .views.General import views, Register
from .views.Curriculo.Inclusion_ingenieria_aula import InclusionIngenieriaAulaListView
from .views.Curriculo.Desarrollo_ciudadania_digital import DesarrolloCiudadaniaDigitalListView
from .views.EscuelaComunidadYPertenencia import CompromisodelaComunidadListView
from .views.Curriculo.ConsideracionesSobreAreasYAsignaturas import ConsideracionesSobreAreasyAsignaturasListView

# GENERAL
urlpatterns= [
    path('', views.CriterioList.as_view() , name= 'criterio_list'),
    path('instituciones/', Register.RegisterListView.as_view(), name= 'register_list'),
    path('instituciones/<int:pk>', Register.RegisterListDetail.as_view(), name= 'register_detail')
]

urlpatterns += [
    # INFRAESTRUCTURA

    # CURRICULO
    # 2.1 Consideraciones sobre Áreas y Asignaturas
    path("consideraciones_sobre_las-areas-y-las-asignaturas/", ConsideracionesSobreAreasyAsignaturasListView.as_view(), name="ConsideracionesSobreAreasYAsignaturas_list"),

    # 2.2 Inclusion_ingenieria_aula
    path('inclusion-ingenieria-aula/', InclusionIngenieriaAulaListView.as_view(), name='inclusion_ingenieria_aula_list'),

    # 2.3 Desarrollo ciudadania digital
    path('desarrollo-ciudadania-digital/', DesarrolloCiudadaniaDigitalListView.as_view(), name='desarrollo_ciudadania_digital_list'),

    # FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN

    # PERSONAL DOCENTE Y ADMINISTRATIVO

    # ESCUELA COMUNIDAD Y PERTENENCIA
    path("escuela-comunidad-y-pertenencia", CompromisodelaComunidadListView.as_view(), name="Escuelacomunidadypertenencia"),
    
    
]
