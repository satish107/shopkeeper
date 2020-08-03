from rest_framework import serializers
from shop.models import ShopCategory, Shop

class ShopSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shop
		fields = ['name', 'slug', 'owner', 'address', 'image', 'description', 'category', 'opening_date', 'added_on', 'updated_on']
