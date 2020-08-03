# from django.conf.urls import url, include
# from api import views as api_view
# from rest_framework.routers import SimpleRouter

# router = SimpleRouter()

# app_name = 'api'
# urlpatterns = [
# 	url(r'^api/', include(router.urls)),
# 	url(r'^api/api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
# 	url(r'^api/shop-list/', api_view.ShopListView.as_view(), name = 'api.shop_list'),
# ]


# from django.conf.urls import url, include
# from django.contrib import admin
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^users/', include('users.urls', namespace = 'users')),
#     url(r'^landing/', include('landing.urls', namespace = 'landing')),
#     url(r'^shop/', include('shop.urls', namespace = 'shop')),
#     url(r'^product/', include('product.urls', namespace = 'product')),
#     url(r'^', include('api.urls', namespace = 'api')),
    
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
