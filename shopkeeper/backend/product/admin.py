from django.contrib import admin
from product.models import Product, ProductCategory

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'category', 'description', 'price', 'stock', 'available']
	list_filter = ['added_on', 'updated_on']
admin.site.register(Product, ProductAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	list_filter = ['added_on', 'updated_on']
admin.site.register(ProductCategory, ProductCategoryAdmin)