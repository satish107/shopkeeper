from rest_framework import serializers
from shop.models import ShopCategory, Shop
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['id', 'email']


class ShopSerializer(serializers.ModelSerializer):
	owner = UserProfileSerializer(many = False, read_only = True)
	class Meta:
		model = Shop
		fields = ['name', 'slug', 'owner', 'address', 'image', 'description', 'category', 'opening_date', 'added_on', 'updated_on']
