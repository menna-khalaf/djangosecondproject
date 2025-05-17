from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_deleted']
    list_filter = ['is_deleted']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'sku', 'is_deleted']
    list_filter = ['category', 'is_deleted']
    search_fields = ['name', 'sku']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock']
