from django.contrib import admin
from .models import Product, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """determines how category details are displayed in the admin panel"""
    list_display = ('name',)

    ordering_by = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """determines how product details are displayed in the admin panel"""
    list_filter = ('category',)
    list_display = ('name', 'category', 'price',)
    search_fields = ['name', 'category']

    ordering_by = ('price',)
