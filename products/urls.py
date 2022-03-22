from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<category_name>', views.chosen_category, name='category'),
    path('<product_id>', views.product_info, name='product_info'),
]
