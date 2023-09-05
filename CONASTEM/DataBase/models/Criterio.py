from django.db import models
from django.db.models import Case, Value, When

class Criterio(models.Model):

    NAME_CHOICE = (
        (1, "INFRAESTRUCTURA"),
        (2, "CURRÍCULO"),
        (3, "FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN"),
        (4, "PERSONAL DOCENTE Y ADMINISTRATIVO"),
        (5, "ESCUELA, COMUNIDAD Y PERTENENCIA")
    )

    name = models.CharField(max_length=5, choices= NAME_CHOICE, primary_key= True)