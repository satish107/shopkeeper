from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from shop.models import Shop
from api.serializers import ShopSerializer
from api.response import SuccessResponse
from rest_framework.response import Response 

# Create your views here.

class ShopListView(APIView):

	def get(self, request, format = None):
		shop_list = Shop.objects.all().order_by('-added_on')
		serializer = ShopSerializer(shop_list, many = True)
		# print(request.__dict__)
		return SuccessResponse(serializer.data)

	def post(self, request, format = None):
		print(request.data)
		serializer = ShopSerializers(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ShopDetailView(APIView):

	def get(self, request, pk, format = None):
		shop_instance = get_object_or_404(Shop, pk = pk)
		serializer = ShopSerializer(shop_instance)
		return SuccessResponse(serializer.data)

