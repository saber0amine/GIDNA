from django.db import models
from lists.models import Projet
from lists.models import Nature
from django.contrib.auth.models import User

class Objectif(models.Model):
    obj = models.CharField(max_length=10000, null=True)
    
    projet = models.ForeignKey(Projet, null=True,  on_delete=models.CASCADE, related_name='objectifs_projet')
    date_objectif = models.DateTimeField(null=True)
    nature = models.ForeignKey(Nature, null=True, on_delete=models.SET_NULL, related_name='objectifs_nature')
    user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.obj
