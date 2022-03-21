from django.contrib import admin
from .models import Product, Category

# Register your models here.
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """determines how product details are displayed in the admin panel"""
    list_filter = ('category',)
    list_display = ('name', 'category', 'price', 'rating')
    search_fields = ['name', 'category']
