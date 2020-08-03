from django.conf.urls import url, include
from api import views as api_view
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^api/api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
	url(r'^api/shop-list/', api_view.ShopListView.as_view(), name = 'api.shop_list'),
]