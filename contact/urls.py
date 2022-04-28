from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('queries/', views.view_queries, name='queries'),
]
