from django.contrib import admin
from bugers.models import Burger

# Register your models here.

@admin.register(Burger)
class BugerAdmin(admin.ModelAdmin):
    pass