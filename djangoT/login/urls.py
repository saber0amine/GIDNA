from django.urls import path
from . import views
urlpatterns = [
    path('', views.flogin , name="acces"),
    path('inscription', views.finscription , name="inscription"),
    path('quitter', views.flogout , name="quitter"),

]
