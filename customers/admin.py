from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'representative_name','company_number', 'created_at','updated_at')
    ordering=('-created__at',)
