from django.shortcuts import render
from rest_framework.views import APIView
from shop.models import Shop
from api.serializers import ShopSerializer

from api.response import success_response

# Create your views here.

class ShopListView(APIView):

	def get(self, request):
		shop_list = Shop.objects.all().order_by('-added_on')
		serializer = ShopSerializer(shop_list, many = True)
		return success_response(serializer.data)
