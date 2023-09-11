from django.db import models
from django.urls import reverse


class Register (models.Model):

    institution_name = models.CharField(max_length= 100, help_text= "Ingrese el nombre de la institución")
    nit = models.CharField(max_length=10, help_text="Ingrese el NIT de la institución")
    adress = models.CharField(max_length=250, help_text="Ingrese la dirección de la institución")
    institution_responsable = models.CharField(max_length= 50, blank= True, null= True, help_text="Ingrese el representante de la institución")
    phone = models.IntegerField(help_text="Ingrese el teléfono de la institución")
    email = models.EmailField (help_text="Ingrese el email principal de la institución")

    PRIORITY_MODEL_CHOICE = (
        ("Exploratorio", "Exploratorio"),
        ("Introductorio", "Introductorio"),
        ("Inmerción parcial", "Inmerción parcial"),
        ("Inmerción completa", "Inmerción completa"),
    )

    model = models.CharField ()

    class Meta:
        verbose_name = ("Formulario de registro de institucion")
        verbose_name_plural = ("Formulario de registro de instituciones")

    def __str__(self):
        return self.institution_name

    def get_absolute_url(self):
        return reverse("register_detail", kwargs={"pk": self.pk})
