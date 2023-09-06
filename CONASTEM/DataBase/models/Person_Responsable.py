from django.db import models



class PersonResponsable (models.Model):
   
    firs_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    email=models.EmailField(max_length=200)