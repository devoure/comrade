from django.contrib import admin
from .models import Enrol

# Register your models here.
@admin.register(Enrol)
class EnrolAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'semester', 'enrol_status']
