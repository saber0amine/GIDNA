from django.urls import path
from . import views
urlpatterns = [
    path('', views.fobj, name='objectif'),
    path('create_objectif/', views.create_objectif, name='create_objectif'),
    path('update-objectif/<int:pk>', views.update_objectif, name='update-objectif'),
    path('delete-objectif/<int:pk>', views.delete_objectif, name="delete-objectif"),
]
