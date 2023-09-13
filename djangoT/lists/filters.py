import django_filters
from .models import Projet , Emplacement , Nature

class filtrer_par_projet(django_filters.FilterSet):
    class Meta:
         model=Projet
         fields = ['projet' ]
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, prefix=prefix)
        self.request = request

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(user=self.request.user)
    
    

class filtrer_par_nature(django_filters.FilterSet):
    class Meta:
         model=Nature
         fields = ['nature' ]
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, prefix=prefix)
        self.request = request

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(user=self.request.user)
    
    
        
class filtrer_par_emplacement(django_filters.FilterSet):
    class Meta:
         model=Emplacement
         fields = ['emplacement' ]
    def __init__(self, data=None, queryset=None, *, request=None, prefix=None):
        super().__init__(data=data, queryset=queryset, prefix=prefix)
        self.request = request

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(user=self.request.user)