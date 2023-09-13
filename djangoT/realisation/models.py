from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Realisation(models.Model):
     livrable = models.FileField(upload_to='livrables/')
     date_realisation = models.DateTimeField(auto_now_add=True , null=True) 
     obj = models.ForeignKey('objectif.Objectif', null=True, on_delete=models.CASCADE)
     tache = models.ForeignKey('planification.Planification', null=True, on_delete=models.CASCADE, related_name='realisations_tache')
     projet = models.ForeignKey('lists.Projet', null=True, on_delete=models.CASCADE)
     emplacement = models.ForeignKey('lists.Emplacement', null=True, on_delete=models.SET_NULL)
     hrs_est = models.ForeignKey('planification.Planification', on_delete=models.CASCADE, related_name='realisations_hrs_est')
     hr_attr = models.FloatField(max_length=10000, null=True)
     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
     def __str__(self):
         return f"Realisation {self.id} - Project: {self.projet}"

   