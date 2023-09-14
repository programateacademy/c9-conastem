from django.db import models
from django.urls import reverse
from django.utils import timezone


class Register (models.Model):


    id = models.AutoField(primary_key=True)
    institution_name = models.CharField(max_length= 100, help_text= "Ingrese el nombre de la institución")
    nit = models.CharField(max_length=10, help_text="Ingrese el NIT de la institución")
    adress = models.CharField(max_length=250, help_text="Ingrese la dirección de la institución")
    institution_responsable = models.CharField(max_length= 50, blank= True, null= True, help_text="Ingrese el representante de la institución")
    phone = models.CharField(max_length=15, help_text="Ingrese el teléfono de la institución")
    email = models.EmailField (max_length=200, help_text="Ingrese el email principal de la institución")
    year = models.IntegerField (help_text="Ingrese el año de registro")

    PRIORITY_MODEL_CHOICE = (
        ("Exploratorio", "Exploratorio"),
        ("Introductorio", "Introductorio"),
        ("Inmerción parcial", "Inmerción parcial"),
        ("Inmerción completa", "Inmerción completa"),
    )

    model = models.CharField (choices=PRIORITY_MODEL_CHOICE, max_length=18)
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = ("Formulario de registro de institucion")
        verbose_name_plural = ("Formulario de registro de instituciones")

    def __str__(self):
        return self.institution_name

    def get_absolute_url(self):
        return reverse("register_detail", args=[str(self.id)])
