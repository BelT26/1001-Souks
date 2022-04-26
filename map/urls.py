from django.urls import path
from . import views

urlpatterns = [
    path('', views.loction_map, name='map'),
    path('<str:city_name>', views.city_detail, name='city_detail'),
    path('add_maker/', views.add_maker, name='add_maker'),
    path('edit_maker/<int:maker_id>/', views.edit_maker,
         name='edit_maker'),
    path('delete_maker/<int:maker_id>/', views.delete_maker,
         name='delete_maker'),
]
