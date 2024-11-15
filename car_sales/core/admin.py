from django.contrib import admin

# Register your models here.
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'price', 'user', 'date_added')  # Columns to display in the list view
    search_fields = ('name', 'model')  # Add search functionality for 'name' and 'model'
    list_filter = ('price', 'date_added')  # Add filters for 'price' and 'date_added'
    ordering = ('-date_added',)  # Order the cars by date_added in descending order

# Register the Car model with custom settings
admin.site.register(Car, CarAdmin)