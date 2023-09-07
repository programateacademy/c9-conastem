from django.db import models


class PersonResponsable (models.Model):
   
   first_name=models.CharField(max_length=100, help_text="Ingrese primer nombre")
   last_name=models.CharField(max_length=100, help_text="Ingrese primer apellido")
   phone_number=models.CharField(max_length=15, help_text= "+XX XXX XX XX")
   email=models.EmailField(max_length=200, default='example@example.com')

   def __str__(self):
      return self.last_name +" "+ self.first_name