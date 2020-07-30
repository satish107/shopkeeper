from django.contrib import admin
from .models import Shop, ShopCategory

# Register your models here.

class ShopAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'owner', 'address', 'description', 'opening_date']
	populated_fields = {'slug': ('name',)}
	list_filter = ['added_on', 'updated_on']
	list_editable = ['address']
admin.site.register(Shop, ShopAdmin)


class ShopCategoryAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug', 'description']
	list_filter = ['added_on', 'updated_on']
admin.site.register(ShopCategory, ShopCategoryAdmin)


