from django.contrib import admin
from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)} # поля, которые будут заполнены автоматически


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category') # фильтр товаров в админке
    list_editable = ('price', 'available') # возможно изменять не переходя в сам товар
    prepopulated_fields = {'slug': ('name',)} # поля, которые будут заполнены автоматически





