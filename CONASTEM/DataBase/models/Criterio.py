from django.db import models
from django.db.models import Case, Value, When
import uuid

class Criterio(models.Model):

    NAME_CHOICE = (
        ("1000", "INFRAESTRUCTURA"),
        ("2000", "CURRÍCULO" ),
        ("3000", "FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN"),
        ("4000", "PERSONAL DOCENTE Y ADMINISTRATIVO"),
        ("5000", "ESCUELA, COMUNIDAD Y PERTENENCIA")
    )

    name = models.CharField(max_length=100, choices= NAME_CHOICE, default="INFRAESTRUCTURA", unique= True)

    def __str__(self):
        return self.name