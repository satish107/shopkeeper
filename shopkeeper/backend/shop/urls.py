from django.conf.urls import url
from shop.views import shop_list, shop_detail, shop_create, shop_edit
app_name = 'shop'
urlpatterns = [
    url(r'^$', shop_list, name = 'shop_list'),
    url(r'^shop/(?P<shop_category_slug>[-\w]+)/$', shop_list, name = 'shop_list_category'),
    url(r'^create-shop/$', shop_create, name = 'shop_create'),
    url(r'^edit/(?P<slug>[-\w]+)/$', shop_edit, name = 'shop_edit'),
    url(r'^detail/(?P<slug>[-\w]+)/$', shop_detail, name = 'shop_detail'),
]