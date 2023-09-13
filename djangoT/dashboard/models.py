from django.db import models
# Create your models here.
from lists.models import Projet  # Import your Project model
from realisation.models import Realisation  # Import your Project model
from django.contrib.auth.models import User


class Dashboard(models.Model):
    task_realiser = models.IntegerField(null=True)
    task_non_realiser = models.IntegerField(null=True)
    total_task_count=models.IntegerField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line to associate the stats with a user

    def update_stats(self):
        self.task_realiser = Realisation.objects.filter(user=self.user).count()
        self.total_task_count = Planification.objects.filter(user=self.user).count()
        if(self.task_realiser <= self.total_task_count ) :  
          self.task_non_realiser = Planification.objects.filter(user=self.user).count() - self.task_realiser # for the calcul of chart
        self.save()



class ProjectStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    total_projects = models.IntegerField(null=True)
    # Add more fields as needed

    def update_stats(self):
        # Filter projects by the associated user
        self.total_projects = Projet.objects.filter(user=self.user).count() 
        self.save()


from planification.models import Planification  # Import your Task model

class TaskStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    total_tasks = models.IntegerField(null=True)
    # Add more fields as needed

    def update_stats(self):
        # for calcul of the total number of task that exist in the planification app
        total_task_count = Planification.objects.filter(user=self.user).count()
        print(f"Total Task Count for User {self.user.username}: {total_task_count}")  # Add this line for debugging
        self.total_tasks = total_task_count
        # Update other fields as needed
        self.save()


from objectif.models import Objectif  # Import your Objective model

class ObjectiveStats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line to associate the stats with a user
    total_objectives = models.IntegerField(null=True)
    # Add more fields as needed

    def update_stats(self):
        self.total_objectives = Objectif.objects.filter(user=self.user).count()
        # Update other fields as needed
        self.save()
