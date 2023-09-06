from django.db import models



class PersonResponsable (models.Model):
   
     first_name=models.CharField(max_length=100,default="")
     last_name=models.CharField(max_length=100,default="")
     phone_number=models.CharField(max_length=20,default="")
     email=models.EmailField(max_length=200, default='example@example.com')

     def __str__(self):
        return self.last_name +" "+ self.first_name