import django_filters
from .models import Objectif


class objectif_filtrer(django_filters.FilterSet):
    date_objectif = django_filters.DateFromToRangeFilter()
    class Meta:
         model=Objectif
         fields = ['projet' , 'date_objectif'  , 'nature' , 'obj']
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.queryset = Objectif.objects.filter(user=user)