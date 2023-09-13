from django.urls import path
from . import views
urlpatterns = [
    path('', views.fplan , name='planification'),
    path('create_tache/', views.create_tache , name='create_tache'),
    path('update-tache/<int:pk>', views.update_tache, name='update-tache'),
    path('delete-tache/<int:pk>', views.delete_tache, name="delete-tache"),

]
