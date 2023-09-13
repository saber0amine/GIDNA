from django.db import models

class CalendarEntry(models.Model):
    DATE_CHOICES = [
        ('T', 'Travail'),
        ('F', 'Férié'),
        ('CP', 'Congé Payé'),
        ('R', 'Récupération'),
        ('M', 'Maladie'),
        ('A', 'Absence'),
    ]

    date = models.DateField()
    working_mode = models.CharField(max_length=2, choices=DATE_CHOICES)
    project_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
