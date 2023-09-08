from django.urls import path
from .views import views


urlpatterns= [
    path('', views.CriterioList.as_view(), name= 'criterio_list'),
]