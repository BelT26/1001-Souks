from django.urls import path
from . import views

urlpatterns = [
    path('', views.loction_map, name='map'),
    path('<city_name>', views.city_detail, name='city_detail')
]
