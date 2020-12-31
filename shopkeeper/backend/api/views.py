from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from shop.models import Shop
from api.serializers import ShopSerializer
from api.response import SuccessResponse
from rest_framework.response import Response
from rest_framework import permissions, authentication
from rest_framework import status

# Create your views here.

class ShopListView(APIView):

	# authentication_classes = (
	# 	authentication.TokenAuthentication,
	# 	authentication.SessionAuthentication
	# )

	# permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def get(self, request, format = None):
		shop_list = Shop.objects.all().order_by('-added_on')
		serializer = ShopSerializer(shop_list, many = True)
		return SuccessResponse(serializer.data)

	def post(self, request, format = None):
		serializer = ShopSerializer(data = request.data)
		if serializer.is_valid():
			print('true')
			serializer.save(owner=request.user)
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ShopDetailView(APIView):

	def get_object(self, pk):
		try:
			return Shop.objects.get(pk=pk)
		except Shop.DoesNotExist:
			return Http404

	def get(self, request, pk, format = None):
		shop_instance = get_object_or_404(Shop, pk = pk)
		serializer = ShopSerializer(shop_instance)
		return SuccessResponse(serializer.data)

	def put(self, request, pk, format = None):
		shop_instance = get_object_or_404(Shop, pk = pk)
		serializer = ShopSerializer(shop_instance, data = request.data)
		if serializer.is_valid():
			print('true')
			serializer.save()
			return Response(serializer.data, status = status.HTTP_201_CREATED)
		return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

from users.models import UserProfile
from api.serializers import UserProfileSerializer
class UsersApi(APIView):
	def get(self, request, format=None):
		user_list = UserProfile.objects.all()
		serializer = UserProfileSerializer(user_list, many=True)
		return SuccessResponse(serializer.data)






