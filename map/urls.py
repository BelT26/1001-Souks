from django.urls import path
from . import views

urlpatterns = [
    path('', views.loction_map, name='map'),
    path('<str:city_name>', views.city_detail, name='city_detail'),
    path('add_maker/', views.add_maker, name='add_maker'),
]
