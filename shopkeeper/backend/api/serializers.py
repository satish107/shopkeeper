from rest_framework import serializers
from shop.models import ShopCategory, Shop
from users.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):
	shops = serializers.PrimaryKeyRelatedField(queryset=Shop.objects.all(), many=True)
	class Meta:
		model = UserProfile
		fields = ['id', 'email', 'shops']

	# def get_shops(self, obj):
	# 	return Shop.objects.filter(owner=obj)


class ShopSerializer(serializers.ModelSerializer):
	# owner = UserProfileSerializer(many = False, read_only = True)
	# users = serializers.StringRelatedField(many=True)
	class Meta:
		model = Shop
		fields = ['name', 'slug', 'address', 'image', 'description', 'category', 'opening_date', 'added_on', 'updated_on']
