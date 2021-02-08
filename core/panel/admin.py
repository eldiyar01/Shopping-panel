from django.contrib import admin
from .models import Date, Product


@admin.register(Date)
class AdminDate(admin.ModelAdmin):
    pass


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    pass
