from django.db import models

class Auditory(models.Model):
     pass  
     InternalAuditDate=models.CharField(max_length=30, default=" ")
     InternalAuditObservations=models.CharField(max_length=500,default=" ")
     external_audit_date=models.CharField(max_length=30,default=" ")
     external_audit_observations=models.CharField(max_length=500,default=" ")

     def __str__(self):
        return "Interna "+ self.InternalAuditDate +". Externa:" +self.external_audit_date

