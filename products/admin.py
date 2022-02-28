from django.contrib import admin

from products.models import Product, ProductCategory

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = [('name', 'price'), 'image', 'text', ('category', 'quantity')]
    search_fields = ['name']
    ordering = ['-price']