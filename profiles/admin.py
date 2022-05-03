from django.contrib import admin
from .models import UserProfile


# Register your models here.
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """determines how profile details are displayed in the admin panel"""
    list_display = ('user', 'default_email')

    
