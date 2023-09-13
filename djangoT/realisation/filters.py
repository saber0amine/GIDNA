import django_filters
from .models import Realisation

class realisation_filtrer(django_filters.FilterSet):
    class Meta:
         model=Realisation
         fields = ['projet'  ,'tache' , 'obj' ,'emplacement' ]
