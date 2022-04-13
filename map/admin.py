from django.contrib import admin
from .models import City


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """determines how category details are displayed in the admin panel"""
    list_display = ('name',)
    ordering_by = ('name',)
