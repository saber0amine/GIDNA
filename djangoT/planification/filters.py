import django_filters
from .models import Planification

class planification_filtrer(django_filters.FilterSet):
    class Meta:
         model=Planification
         fields = ['projet'  ,'livrable' , 'obj' ,'tache' ]
