from django.urls import path

# GENERAL
from .views.General import views, Register

# INFRAESTRUCTURA
from .views.Infraestructura import InfraestructuraListView
from .views.Infraestructura import AmbienteEscolarListView
from .views.Infraestructura import DesarrolloDeEquiposLideresListView
from .views.Infraestructura import EquidadListView
from .views.Infraestructura import PlaneacionInstitucionalListView
from .views.Infraestructura import RecursosTecnologicosListView
from .views.Infraestructura import SostenibilidadListView
# from .views.Infraestructura import UsoDeInformacionListView


# CURRICULO
from .views.Curriculo import InclusionIngenieriaAulaListView
from .views.Curriculo import DesarrolloCiudadaniaDigitalListView
from .views.Curriculo import CurriculoProgresivoListView
from .views.Curriculo import CurriculoPropioListView
from .views.Curriculo import EvaluacionEstudiantesListView

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .views import Formacion_Instruccion_Evaluacion

# PERSONAL DOCENTE Y ADMINISTRATIVO

# ESCUELA COMUNIDAD Y PERTENENCIA
from .views.EscuelaComunidadYPertenencia import CompromisodelaComunidadListView
from .views.EscuelaComunidadYPertenencia import ConvivenciaescolarListView
from .views.EscuelaComunidadYPertenencia import EscuelaComunidadyPertenenciaListView
from .views.EscuelaComunidadYPertenencia import RelacionesconlaComunidadListView
from .views.EscuelaComunidadYPertenencia import SostenibilidadEscuelaComunidadyPertenenciaListView


# GENERAL
urlpatterns= [
    path ('', Register.index, name= 'index'),
    path ('home/', views.home , name= 'home'),
    path("criterios/", views.CriterioList.as_view(), name="criterio_list"),
    path ('instituciones/', Register.RegisterListView.as_view(), name= 'register_list'),
    path ('instituciones/<int:pk>', Register.RegisterListDetail.as_view(), name= 'register_detail')
]

urlpatterns += [
    # #INFRAESTRUCTURA
    path("infraestructura/", InfraestructuraListView.as_view(),name="Infraestructura"),
    path("ambiente-escolar/", AmbienteEscolarListView.as_view(), name="Ambiente_escolar_list"),
    path("desarrollo-de-equipos-lideres/", DesarrolloDeEquiposLideresListView.as_view(), name="Desarrollo_de_equipos_lideres_list"),
    path("equidad/", EquidadListView.as_view(), name="Equidad_list"),
    path("planeacion-institucional/", PlaneacionInstitucionalListView.as_view(), name="Planeacion_institucional_list" ),
    path("recursos-tecnologicos/", RecursosTecnologicosListView.as_view(), name="Recursos_tecnologicos_list" ),
    path("sostenibilidad/", SostenibilidadListView.as_view(), name="Sostenibilidad_list" ),
    # path("uso-de-info/", UsoDeInformacionListView.as_view(), name="Uso_de_info_list" ),  
]

urlpatterns += [
    
    # CURRICULO
        # 2.2 Inclusion ingenieria aula
    path('inclusion-ingenieria-aula', InclusionIngenieriaAulaListView.as_view(), name='Inclusion_ingenieria_aula_list'),
        # 2.3 Desarrollo ciudadania digital
    path ('desarrollo-ciudadania-digital', DesarrolloCiudadaniaDigitalListView.as_view(), name='Desarrollo_ciudadania_digital_list'),
        # 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
    path ('curriculo-progresivo', CurriculoProgresivoListView.as_view(), name='Curriculo_progresivo_list'),
        # 2.6 CURRÍCULO PROPIO
    path ('curriculo-propio', CurriculoPropioListView.as_view(), name='Curriculo_propio_list'),
        # 2.8 EVALUACIÓN DE LOS ESTUDIANTES
    path ('evaluacion-estudiantes', EvaluacionEstudiantesListView.as_view(), name='Evaluacion_estudiantes_list'),

    # FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
    path('formacion-instruccion-evaluacion/new', Formacion_Instruccion_Evaluacion.data_new, name='data_new'),
    path("formacion-instruccion-evaluacion/", Formacion_Instruccion_Evaluacion.FormacionInstruccionEvaluacionListView.as_view(), name="FormacionInstruccionEvaluacion"),
    path('aprendizaje-centrado', Formacion_Instruccion_Evaluacion.AprendizajeCentradoListView.as_view(), name='aprendizaje_centrado_detail'),

    # PERSONAL DOCENTE Y ADMINISTRATIVO

    # ESCUELA COMUNIDAD Y PERTENENCIA
    path("escuelacomunidadypertenencia", EscuelaComunidadyPertenenciaListView.as_view(),name="Escuelacomunidadypertenencia"),
    path("compromisodelacomunidad", CompromisodelaComunidadListView.as_view(), name="Compromisodelacomunidad_List"),
    path("convivenciaescolar", ConvivenciaescolarListView.as_view(), name="Convivenciaescolar_List"),
    path("relacionesconlacomunidad", RelacionesconlaComunidadListView.as_view(), name="Relacionesconlacomunidad_List"),
    path("sostenibilidadescuelacomunidadypertenencia", SostenibilidadEscuelaComunidadyPertenenciaListView.as_view(), name="Sostenibilidadescuelacomunidadypertenecia_List" ),   
]