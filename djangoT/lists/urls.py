from django.urls import path
from . import views
urlpatterns = [
    path('', views.flists , name='lists'),
    path('create_projet/', views.create_projet, name='create_projet'),
    path('create_nature/', views.create_nature, name='create_nature'),
    path('create_emplacement/', views.create_emplacement, name='create_emplacement'),
    path('update-projet/<int:pk>', views.update_projet, name='update-projet'),
    path('delete-projet/<int:pk>', views.delete_projet, name="delete-projet"),
    path('update-nature/<int:pk>', views.update_nature, name='update-nature'),
    path('delete-nature/<int:pk>', views.delete_nature, name="delete-nature"),
    path('update-emplacement/<int:pk>', views.update_emplacement, name='update-emplacement'),
    path('delete-emplacement/<int:pk>', views.delete_emplacement, name="delete-emplacement"),


]
