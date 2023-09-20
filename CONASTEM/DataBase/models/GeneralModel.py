from django.db import models
from django.urls import reverse
from .Person_Responsable import PersonResponsable

class GeneralModel (models.Model):

    priority = models.IntegerField (null=True, help_text="Ingrese el nivel de prioridad del 1 al 10 para el numeral")
    
    dep_responsable = models.CharField (max_length=30, default= "Dirección")
    
    person_responsable = models.ForeignKey(PersonResponsable, on_delete= models.PROTECT)
    
    track_date = models.DateField(verbose_name='Fecha de seguimiento', default="YYYY-MM-DD")
    
    internal_auditory_date = models.DateField(default="YYYY-MM-DD", null= True, blank=True)
    internal_auditory_obs = models.TextField(max_length=1000, blank= True)

    external_auditory_date = models.DateField(default="YYYY-MM-DD", null= True, blank= True)
    external_auditory_obs = models.TextField(max_length=1000, blank= True)

    evidence = models.URLField(blank= True, help_text= 'Ingrese sus evidencias aquí')
    
    created_at = models.DateTimeField(auto_now_add= True) 
    updated_at = models.DateTimeField(auto_now= True)

    class Meta:
        abstract = True



