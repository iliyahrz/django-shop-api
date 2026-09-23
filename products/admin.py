from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title', )}

@admin.register(Product)
class Productadmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'price', 'is_active']
    prepopulated_fields = {'slug': ('title', )}