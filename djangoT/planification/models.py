from django.db import models
from django.contrib.auth.models import User

class Planification(models.Model):
    tache = models.CharField(max_length=10000, null=True)
    hrs_est = models.FloatField(max_length=10000, null=True)
    livrable = models.CharField(max_length=10000, null=True)
    date_tache = models.DateTimeField(auto_now_add=True, null=True)
    obj = models.ForeignKey('objectif.Objectif', null=True, on_delete=models.CASCADE)
    projet = models.ForeignKey('lists.Projet', null=True, on_delete=models.CASCADE)
    nature = models.ForeignKey('lists.Nature',on_delete=models.SET_NULL , null=True)
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

    def __str__(self):
         return self.tache
