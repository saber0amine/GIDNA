from django.contrib import admin
from .models import ProjectStats
from .models import Dashboard
from .models import TaskStats
from .models import ObjectiveStats

# Register your models here.

admin.site.register(Dashboard)
admin.site.register(ProjectStats)
admin.site.register(TaskStats)
admin.site.register(ObjectiveStats)