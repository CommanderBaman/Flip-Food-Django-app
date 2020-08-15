from django.contrib import admin

# Register your models here.
from .models import FoodInfo, Cart

admin.site.register( FoodInfo)
admin.site.register( Cart)