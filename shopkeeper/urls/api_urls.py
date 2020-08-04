from django.conf.urls import url, include
from api import views as api_view
from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

router = SimpleRouter()

urlpatterns = [
	url(r'^api/', include(router.urls)),
	url(r'^api/api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
	url(r'^api/shop-list/', api_view.ShopListView.as_view(), name = 'api.shop_list'),
	url(r'^api/(?P<pk>\d+)/shop/', api_view.ShopDetailView.as_view(), name = 'api.shop_detail')
]
urlpatterns = format_suffix_patterns(urlpatterns)