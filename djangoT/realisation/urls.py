from django.urls import path
from . import views
urlpatterns = [
    path('', views.freal , name='realisation'),
    path('valider_realisation/', views.valider_realisation , name='valider_realisation'),
    path('realisation/<int:pk>', views.singular_realisation, name="realisation"),

 
]
