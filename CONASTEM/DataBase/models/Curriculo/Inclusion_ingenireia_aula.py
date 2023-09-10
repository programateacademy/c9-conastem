from django.db import models
from django.urls import reverse
from django.utils import timezone  # Import timezone

from ..Person_Responsable import PersonResponsable
from ...models.Criterio import Criterio

# 2.2 INCLUSION DE LA INGENIERIA EN EL AULA
class Inclusion_ingenieria_aula(models.Model):
    criterio = models.ForeignKey(Criterio, on_delete=models.SET_NULL, null=True)

    ITEM_CHOICE = [
        ("221", "Inclusión del proceso de diseño en ingeniería en el currículo."),
        ("222", "Los docentes de la mayoría de las asignaturas adoptan el proceso de diseño como parte fundamental del desarrollo pedagógico."),
        ("223", "El proceso de diseño se ejecuta de forma intencional dado el potencial pedagógico de cada una de sus fases."),
        ("224", "Las actividades se diseñan con el objetivo de incluir el pensamiento computacional y el pensamiento matemático en la gran mayoría de las asignaturas."),
        ("225", "Actividades de prototipado en espacios para la creatividad (Maker Spaces)"),
    ]

    numeral = models.CharField(max_length=1000, choices=ITEM_CHOICE)

    PRIORITY_MODEL_CHOICE = (
        ("Exploratorio", "Exploratorio"),
        ("Introductorio", "Introductorio"),
        ("Inmersión parcial", "Inmersión parcial"),
        ("Inmersión completa", "Inmersión completa"),
    )

    priority_model = models.CharField(max_length=20, choices=PRIORITY_MODEL_CHOICE, default="Introductorio")

    dep_responsable = models.CharField(max_length=30, default="Dirección")

    person_responsable = models.ManyToManyField(PersonResponsable, help_text="Seleccione un responsable")

    track_year = models.IntegerField(help_text="Ingrese año de seguimiento")

    track_date = models.CharField(max_length=5, help_text="Ingrese fecha de seguimiento")

    internal_auditory_date = models.DateField(default="2000-01-31", null=True)
    internal_auditory_obs = models.TextField(max_length=1000, blank=True)

    external_auditory_date = models.DateField(default="2000-01-31", null=True, blank=True)
    external_auditory_obs = models.TextField(max_length=1000, blank=True)

    # Add the created_at field with default set to current time
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.numeral

    def get_absolute_url(self):
        return reverse("Inclusion_ingenieria_aula", args=[str(self.id)])
