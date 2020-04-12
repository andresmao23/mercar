from django.contrib import admin
from .models import Category, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated',)
    list_display = ('name','created',)
    search_fields = ['name']
    list_filter = ['created']

class ProductAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated',)
    list_display = ('name','price','created',)
    search_fields = ['name','category_id__name']
    list_filter = ['created']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)