from django.urls import path

# GENERAL
from .views.General import views, Register

# INFRAESTRUCTURA
# from .views.Infraestructura import 

# CURRICULO
from .views.Curriculo import ConsideracionesSobreAreasYAsignaturasListView 
from .views.Curriculo import InclusionIngenieriaAulaListView
from .views.Curriculo import DesarrolloCiudadaniaDigitalListView
from .views.Curriculo import CurriculoProgresivoListView
from .views.Curriculo import CurriculoPropioListView
from .views.Curriculo import EvaluacionEstudiantesListView
from .views.Curriculo import CurriculoListView

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
    # path ('home/', views.home , name= 'home'),
    path("home/", views.CriterioList.as_view(), name="criterio_list"),
    path ('instituciones/', Register.RegisterListView.as_view(), name= 'register_list'),
    path ('instituciones/<int:pk>', Register.RegisterListDetail.as_view(), name= 'register_detail')
]
urlpatterns += [

    # CURRICULO
<<<<<<< HEAD
    # 2.1 Consideraciones sobre Áreas y Asignaturas
    path("consideracionesareasyasignaturas/", ConsideracionesSobreAreasYAsignaturasListView.as_view(), name="ConsideracionesSobreAreasYAsignaturas_list"),
    # 2.2 Inclusion_ingenieria_aula
    path('inclusion-ingenieria-aula/', InclusionIngenieriaAulaListView.as_view(), name='inclusion_ingenieria_aula_list'),
    # 2.3 Desarrollo ciudadania digital
    path('desarrollo-ciudadania-digital/', DesarrolloCiudadaniaDigitalListView.as_view(), name='desarrollo_ciudadania_digital_list'),
    # 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
=======
    path("curriculo/", CurriculoListView.as_view(), name="Curriculo_list"),
        # 2.2 Inclusion ingenieria aula
    path('inclusion-ingenieria-aula', InclusionIngenieriaAulaListView.as_view(), name='Inclusion_ingenieria_aula_list'),
        # 2.3 Desarrollo ciudadania digital
    path ('desarrollo-ciudadania-digital', DesarrolloCiudadaniaDigitalListView.as_view(), name='Desarrollo_ciudadania_digital_list'),
        # 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
>>>>>>> 086d23576202237abc57b644020fed49dd5d7f64
    path ('curriculo-progresivo', CurriculoProgresivoListView.as_view(), name='Curriculo_progresivo_list'),
    # 2.6 CURRÍCULO PROPIO
    path ('curriculo-propio', CurriculoPropioListView.as_view(), name='Curriculo_propio_list'),
    # 2.8 EVALUACIÓN DE LOS ESTUDIANTES
    path ('evaluacion-estudiantes', EvaluacionEstudiantesListView.as_view(), name='Evaluacion_estudiantes_list'),

    # FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
    path('formacion-instruccion-evaluacion/new', Formacion_Instruccion_Evaluacion.data_new, name='data_new'),
    path("formacion-instruccion-evaluacion/", Formacion_Instruccion_Evaluacion.FormacionInstruccionEvaluacionListView.as_view(), name="FormacionInstruccionEvaluacion"),
    path('aprendizaje-centrado', Formacion_Instruccion_Evaluacion.AprendizajeCentradoListView.as_view(), name='aprendizaje_centrado_list'),
    path("educacion-stem-integrada/", Formacion_Instruccion_Evaluacion.EducacionStemIntegradaListView.as_view(), name='educacion_stem_integrada_list'),
    path("tecnologia-para-formacion/", Formacion_Instruccion_Evaluacion.TecnologiaFormacionListView.as_view(), name='tecnologia_para_Formacion_list' ), 
    
    # PERSONAL DOCENTE Y ADMINISTRATIVO

    # ESCUELA COMUNIDAD Y PERTENENCIA
    path("escuelacomunidadypertenencia", EscuelaComunidadyPertenenciaListView.as_view(),name="Escuelacomunidadypertenencia"),
    path("compromisodelacomunidad", CompromisodelaComunidadListView.as_view(), name="Compromisodelacomunidad_List"),
    path("convivenciaescolar", ConvivenciaescolarListView.as_view(), name="Convivenciaescolar_List"),
    path("relacionesconlacomunidad", RelacionesconlaComunidadListView.as_view(), name="Relacionesconlacomunidad_List"),
    path("sostenibilidadescuelacomunidadypertenencia", SostenibilidadEscuelaComunidadyPertenenciaListView.as_view(), name="Sostenibilidadescuelacomunidadypertenecia_List" ),
]