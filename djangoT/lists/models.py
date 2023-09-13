from django.db import models
from login.models import Login
from django.contrib.auth.models import User
# Create your models here.



class Lists(models.Model):
     projet = models.CharField(max_length=200,null=True )
     nature = models.CharField(max_length=200,null=True)
     emplacement = models.CharField(max_length=200,null=True )
     user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
     def __str__(self):
         return self.projet
     
     
    
class Projet(models.Model):
    #  All_projet = models.ForeignKey('lists.Projet', null=True, on_delete=models.CASCADE , related_name='')
     projet = models.CharField(max_length=200)
     user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)

     # name_user = models.ForeignKey(Login,null=True, on_delete=models.SET_NULL)
     def __str__(self):
         return self.projet
     
     
    
class Nature(models.Model):
     nature = models.CharField(max_length=200,null=True)
     user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    #  name_user = models.ForeignKey(Login,null=True, on_delete=models.SET_NULL)
     def __str__(self):
         return self.nature
     
     
class Emplacement(models.Model):
     emplacement = models.CharField(max_length=200,null=True )
     user = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    #  name_user = models.ForeignKey(Login,null=True, on_delete=models.SET_NULL)
     def __str__(self):
         return self.emplacement
     
     