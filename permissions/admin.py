from django.contrib import admin
from .models import ScreenPermission

# Register your models here.
@admin.register(ScreenPermission)
class ScreenPermissionAdmin(admin.ModelAdmin):
    list_display = ('user','screen_name','can_access')
    list_filter =('user','can_access')
    search_field = ('screen_name')