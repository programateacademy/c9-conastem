from django.db import models
from django.db.models import Case, Value, When
import uuid

class Criterio(models.Model):

    NAME_CHOICE = (
        ("INFRAESTRUCTURA" ,"INFRAESTRUCTURA"),
        ("CURRÍCULO","CURRÍCULO" ),
        ("FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN","FORMACIÓN / INSTRUCCIÓN / EVALUACIÓN"),
        ("PERSONAL DOCENTE Y ADMINISTRATIVO","PERSONAL DOCENTE Y ADMINISTRATIVO"),
        ("ESCUELA, COMUNIDAD Y PERTENENCIA", "ESCUELA, COMUNIDAD Y PERTENENCIA")
    )

    name = models.CharField(max_length=100, choices= NAME_CHOICE, default="INFRAESTRUCTURA", primary_key= True, unique=True)

    def __str__(self):
        return self.name