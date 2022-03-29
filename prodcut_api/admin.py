from django.contrib import admin
from .models import Product, Remise 

# Register your models here.

admin.site.register([Product, Remise])