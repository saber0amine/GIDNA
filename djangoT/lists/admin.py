from django.contrib import admin
from .models import Lists
from .models import Projet
from .models import Nature
from .models import Emplacement


# Register your models here.
admin.site.register(Lists)
admin.site.register(Projet)
admin.site.register(Nature)
admin.site.register(Emplacement)

