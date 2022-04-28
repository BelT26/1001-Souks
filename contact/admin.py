from django.contrib import admin
from .models import Query


# Register your models here.
@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    """determines how category details are displayed in the admin panel"""
    list_display = ('date_submitted', 'query_type', 'name',)

    ordering_by = ('date_submitted',)
