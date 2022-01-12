from django.contrib import admin
from .models import Fee

# Register your models here.
@admin.register(Fee)
class Feedmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'fee_balance']
