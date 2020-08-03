from django.conf.urls import url, include
from django.contrib import admin
from shop.views import shop_list
from django.conf import settings
from django.conf.urls.static import static

from .shop_urls import urlpatterns as shop_urlpatterns
from .product_urls import urlpatterns as product_urlpatterns
from .user_urls import urlpatterns as user_urlpatterns
from .landing_urls import urlpatterns as landing_urlpatterns
from .api_urls import urlpatterns as api_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', shop_list, name = 'shop'),
    
]

urlpatterns += shop_urlpatterns
urlpatterns += product_urlpatterns
urlpatterns += user_urlpatterns
urlpatterns += landing_urlpatterns
urlpatterns += api_urlpatterns

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
