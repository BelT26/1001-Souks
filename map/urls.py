from django.urls import path
from . import views

urlpatterns = [
    path('', views.loction_map, name='map'),
]
