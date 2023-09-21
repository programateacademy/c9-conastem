from django.urls import path

# GENERAL
from .views.General import views

# INFRAESTRUCTURA
from .views import Infraestructura
from .views.Infraestructura import InfraestructuraListView
from .views.Infraestructura import AmbienteEscolarListView
from .views.Infraestructura import DesarrolloDeEquiposLideresListView
from .views.Infraestructura import EquidadListView
from .views.Infraestructura import PlaneacionInstitucionalListView
from .views.Infraestructura import RecursosTecnologicosListView
from .views.Infraestructura import SostenibilidadListView
from .views.Infraestructura import UsoDeInformacionListView

# CURRICULO
from .views import Curriculo
from .views.Curriculo import ConsideracionesSobreAreasYAsignaturasListView 
from .views.Curriculo import InclusionIngenieriaAulaListView
from .views.Curriculo import DesarrolloCiudadaniaDigitalListView
from .views.Curriculo import IntegracionCurricularListView
from .views.Curriculo import CurriculoProgresivoListView
from .views.Curriculo import CurriculoPropioListView
from .views.Curriculo import DesarrolloHabilidadesSigloXXIListView
from .views.Curriculo import EvaluacionEstudiantesListView
from .views.Curriculo import SostenibilidadCurriculoListView
from .views.Curriculo import CurriculoListView

# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
from .views import Formacion_Instruccion_Evaluacion
from .views.Formacion_Instruccion_Evaluacion import AprendizajeExtendidoListView
from .views.Formacion_Instruccion_Evaluacion import AprendizajeRigurosoListView
from .views.Formacion_Instruccion_Evaluacion import PlaneacionyCreaciondeActividadesListView
from .views.Formacion_Instruccion_Evaluacion import EstrategiasFormativasListView

# PERSONAL DOCENTE Y ADMINISTRATIVO
from .views.PersonalDocenteYAdministrativo import PersonalDocenteyAdministrativoListView
from .views.PersonalDocenteYAdministrativo import ProfesionalesEspecializadosEducacionSTEMListView
from .views.PersonalDocenteYAdministrativo import DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionalesListView
from .views.PersonalDocenteYAdministrativo import ApoyoPedagogicoListView
from .views.PersonalDocenteYAdministrativo import SostenibilidadDocenteAdministrativoListView

# ESCUELA COMUNIDAD Y PERTENENCIA
from .views import EscuelaComunidadYPertenencia
from .views.EscuelaComunidadYPertenencia import CompromisodelaComunidadListView
from .views.EscuelaComunidadYPertenencia import ConvivenciaescolarListView
from .views.EscuelaComunidadYPertenencia import EscuelaComunidadyPertenenciaListView
from .views.EscuelaComunidadYPertenencia import RelacionesconlaComunidadListView
from .views.EscuelaComunidadYPertenencia import SostenibilidadEscuelaComunidadyPertenenciaListView


# GENERAL
urlpatterns= [
    path ('', views.index, name= 'index'),
    path("home/", views.CriterioList.as_view(), name="criterio_list"),
    path('instituciones/', views.RegisterListView.as_view(), name= 'register_list'),
    path('instituciones/<int:pk>', views.RegisterListDetail.as_view(), name= 'register_detail'),
    path("responsable/new", views.person_responsablenew, name="person_responsablenew"),
    path("responsables/", views.PersonResponsableListView .as_view(), name="responsable_list"),
    path("responsables/<int:pk>", views.PersonResponsableDetail .as_view(), name="responsable_detail"),
]

urlpatterns += [
    # INFRAESTRUCTURA
    path("infraestructura/", InfraestructuraListView.as_view(),name="Infraestructura"),
    path("ambiente-escolar/", AmbienteEscolarListView.as_view(), name="Ambiente_escolar_list"),
    path("ambiente-escolar/new/", Infraestructura.Ambiente_escolar_new, name="Ambiente_escolar_new"),
    path("desarrollo-de-equipos-lideres/", DesarrolloDeEquiposLideresListView.as_view(), name="Desarrollo_de_equipos_lideres_list"),
    path("desarrollo-de-equipos-lideres/new/", Infraestructura.desarrollo_de_equipos_lideres_new, name="Desarrollo_de_equipos_lideres_new"),
    path("equidad/", EquidadListView.as_view(), name="Equidad_list"),
    path("equidad/new/", Infraestructura.Equidad_new, name="Equidad_list"),
    path("planeacion-institucional/", PlaneacionInstitucionalListView.as_view(), name="Planeacion_institucional_list" ),
    path("planeacion-institucional/new/", Infraestructura.Planeacion_institucional_new, name="Planeacion_institucional_list_new" ),
    path("recursos-tecnologicos/", RecursosTecnologicosListView.as_view(), name="Recursos_tecnologicos_list" ),
    path("sostenibilidad/", SostenibilidadListView.as_view(), name="Sostenibilidad_list" ),
    path("sostenibilidad/new/", Infraestructura.Sostenibilidad_new, name="Sostenibilidad_new" ),
    path("recursos-tecnologicos/new/", Infraestructura.Recursos_tecnologicos_new, name="Recursos_tecnologicos_new" ),
    path("uso-de-info/", UsoDeInformacionListView.as_view(), name="Uso_informacion_list" ),  
    path("uso-de-info/new/", Infraestructura.Uso_de_info_new, name="Uso_informacion_new" ),  
]

urlpatterns += [
    # CURRICULO
    path("curriculo/", CurriculoListView.as_view(), name="Curriculo_list"),
    # 2.1 Consideraciones sobre Áreas y Asignaturas
    path("consideraciones-areas-y-asignaturas/", ConsideracionesSobreAreasYAsignaturasListView.as_view(), name="ConsideracionesSobreAreasYAsignaturas_list"),
    path("consideraciones-areas-y-asignaturas/new", Curriculo.ConsideracionesSobreAreasYAsignaturas_new, name="ConsideracionesSobreAreasYAsignaturas_new"),
    # 2.2 Inclusion_ingenieria_aula
    path('inclusion-ingenieria-aula/', InclusionIngenieriaAulaListView.as_view(), name='Inclusion_ingenieria_aula_list'),
    path('inclusion-ingenieria-aula/new', Curriculo.IngenieriaAula_new, name='Inclusion_ingenieria_aula_new'),
    # 2.3 Desarrollo ciudadania digital
    path('desarrollo-ciudadania-digital/', DesarrolloCiudadaniaDigitalListView.as_view(), name='desarrollo_ciudadania_digital_list'),
    path('desarrollo-ciudadania-digital/new', Curriculo.CiudadaniaDigital_new, name='desarrollo_ciudadania_digital_new'),
    # 2.4 Integración curricular
    path('integracion-curricular/', IntegracionCurricularListView.as_view(), name='IntegracionCurricular_list'),
    path('integracion-curricular/new', Curriculo.IntegracionCurricular_new, name='IntegracionCurricular_new'),
    # 2.5 CURRÍCULO PROGRESIVO Y ALINEADO CON LOS ESTÁNDARES CURRICULARES
    path("curriculo-progresivo/", CurriculoProgresivoListView.as_view(), name="Curriculo_progresivo_list"),
    path("curriculo-progresivo/new", Curriculo.CurriculoProgresivo_new, name="Curriculo_progresivo_new"),
    # 2.6 CURRÍCULO PROPIO
    path ('curriculo-propio', CurriculoPropioListView.as_view(), name='Curriculo_propio_list'),
    path ('curriculo-propio/new', Curriculo.CurriculoPropio_new, name='Curriculo_propio_new'),
    # 2.7 Desarrollo ahbilidades siglo XXI
    path('desarrollo-habilidades-siglo-XXI/', DesarrolloHabilidadesSigloXXIListView.as_view(), name='DesarrolloHabilidadesSigloXXI_list'),
    path('desarrollo-habilidades-siglo-XXI/new', Curriculo.DesarrolloHabilidadesSigloXXI_new, name='DesarrolloHabilidadesSigloXXI_new'),
    # 2.8 EVALUACIÓN DE LOS ESTUDIANTES
    path ('evaluacion-estudiantes', EvaluacionEstudiantesListView.as_view(), name='Evaluacion_estudiantes_list'),
    path ('evaluacion-estudiantes/new', Curriculo.EvaluacionEstudiantes_new, name='Evaluacion_estudiantes_new'),
    # 2.9 Sostenibilidad - Curriculo
    path ('sostenibilidad-curriculo/', SostenibilidadCurriculoListView.as_view(), name='SostenibiliadCurriculo_list'),
    path ('sostenibilidad-curriculo/new', Curriculo.SostenibilidadCurriculo_new, name='SostenibiliadCurriculo_new'),
]

urlpatterns += [
# FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN
    path("formacion-instruccion-evaluacion/", Formacion_Instruccion_Evaluacion.FormacionInstruccionEvaluacionListView.as_view(), name="FormacionInstruccionEvaluacion"),
        # 3.1 APRENDIZAJE CENTRADO EN EL ESTUDIANTE
    path('aprendizaje-centrado', Formacion_Instruccion_Evaluacion.AprendizajeCentradoListView.as_view(), name='aprendizaje_centrado_list'),
    path("aprendizaje-centrado/new", Formacion_Instruccion_Evaluacion.Aprendizajecentrado_new, name="aprendizaje_centrado_new"),
        # 3.2 APRENDIZAJE RIGUROSO
    path('aprendizajeriguroso', AprendizajeRigurosoListView.as_view(),name="AprendizajeRiguroso_List"),
    path('aprendizajeriguroso/new', Formacion_Instruccion_Evaluacion.Aprendizajeriguroso_new, name='aprendizajerigurosonew'),
        # 3.3 PLANEACIÓN Y CREACIÓN DE ACTIVIDADES
    path('planeacionycreaciondeactividades', PlaneacionyCreaciondeActividadesListView.as_view(),name="PlaneacionyCreaciondeActividades_List"),
    path('planeacionycreaciondeactividades/new', Formacion_Instruccion_Evaluacion.Planeacionycreaciondeactividades_new, name='planeacionycreaciondeactividadesnew'),
        # 3.4 EDUCACIÓN STEM INTEGRADA
    path("educacion-stem-integrada/", Formacion_Instruccion_Evaluacion.EducacionStemIntegradaListView.as_view(), name='educacion_stem_integrada_list'),
    path("educacion-stem-integrada/new", Formacion_Instruccion_Evaluacion.EducacionSTEM_new, name="educacion_stem_integrada_new"),
        # 3.5 TECNOLOGÍA PARA LA FORMACIÓN / INSTRUCCIÓN
    path("tecnologia-para-formacion/", Formacion_Instruccion_Evaluacion.TecnologiaFormacionListView.as_view(), name='tecnologia_para_Formacion_list'), 
    path("tecnologia-para-formacion/new", Formacion_Instruccion_Evaluacion.TecnologiaFormacion_new , name="tecnologia_para_Formacion_new"),
        # 3.6 ESTRATEGIAS FORMATIVAS
    path('estrategiasformativas', EstrategiasFormativasListView.as_view(), name="EstrategiasFormativas_List"),
    path('estrategiasformativas/new', Formacion_Instruccion_Evaluacion.Estrategiasformativas_new, name='estrategiasformativasnew'),
        # 3.7 ELECCIÓN DE CARRERA
    path("eleccion-carrera/", Formacion_Instruccion_Evaluacion.EleccionCarreraListView.as_view(), name='eleccion_carrera_list'),
    path("eleccion-carrera/new", Formacion_Instruccion_Evaluacion.Eleccioncarrera_new, name="eleccion_carrera_new"),
        # 3.8 APRENDIZAJE EXTENDIDO
    path('aprendizajeextendido', AprendizajeExtendidoListView.as_view(),name="AprendizajeExtendido_List"),
    path('aprendizajeextendido/new', Formacion_Instruccion_Evaluacion.Aprendizajeextendido_new, name='aprendizajeextendidonew'),
        # 3.9 SOSTENIBILIDAD - FORMACIÓN/INSTRUCCIÓN/EVALUACIÓN
    path("sostenibilidad-formacion-instruccion/", Formacion_Instruccion_Evaluacion.SostenibilidadListView.as_view(), name="sostenibilidad_list"),
    path("sostenibilidad-formacion-instruccion/new", Formacion_Instruccion_Evaluacion.SostenibilidadFormacion_new, name="sostenibilidad_new"),
]

urlpatterns += [
    # PERSONAL DOCENTE Y ADMINISTRATIVO
    path("personal-docente-y-administrativo",PersonalDocenteyAdministrativoListView.as_view(), name="PersonalDocenteyAdministrativo"),
    path("profesional-calificado-educacion-stem",ProfesionalesEspecializadosEducacionSTEMListView.as_view(), name="ProfesionalesEspecializadosEducacionSTEM_List"),
    path("desarrollo-profesional-docentes-directores-consejeros-profesionales", DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionalesListView.as_view(), name="DesaProfesionalDocentesDirectoresdeEscuelaConsejerosProfesionales_list"),
    path("apoyo-pedagogico-personal",ApoyoPedagogicoListView.as_view(), name="ApoyoPedagogico_List"),
    path("sostenibilidad-docente-administrativo", SostenibilidadDocenteAdministrativoListView.as_view(), name="SostenibilidadDocenteAdministrativo_List"),
]

urlpatterns += [
    # ESCUELA COMUNIDAD Y PERTENENCIA
    path("escuelacomunidadypertenencia", EscuelaComunidadyPertenenciaListView.as_view(),name="Escuelacomunidadypertenencia"),
    path("compromisodelacomunidad", CompromisodelaComunidadListView.as_view(), name="Compromisodelacomunidad_List"),
    path('compromisodelacomunidad/new', EscuelaComunidadYPertenencia.Compromisodelacomunidad_new, name='compromisodelacomunidadnew'),
    path("convivenciaescolar", ConvivenciaescolarListView.as_view(), name="Convivenciaescolar_List"),
    path('convivenciaescolar/new', EscuelaComunidadYPertenencia.convivenciaescolarnew,name='convivenciaescolarnew'),
    path("relacionesconlacomunidad", RelacionesconlaComunidadListView.as_view(), name="Relacionesconlacomunidad_List"),
    path("relacionesconlacomunidad/new", EscuelaComunidadYPertenencia.relacionesconlacomunidadnew, name='relacionesconlacomunidadnew'),
    path("sostenibilidadescuelacomunidadypertenencia", SostenibilidadEscuelaComunidadyPertenenciaListView.as_view(), name="Sostenibilidadescuelacomunidadypertenecia_List" ),
    path("sostenibilidadescuela/new", EscuelaComunidadYPertenencia.sostenibilidadescuelanew, name='sostenibilidadescuelanew')
    ]

