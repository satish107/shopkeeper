from django.conf.urls import url
from product.views import product_list, product_detail

urlpatterns = [
	url(r'^product/$', product_list, name = 'product_list'),
    url(r'^product-list/(?P<category_slug>[-\w]+)/$', product_list, name = 'product_category_list'),
    url(r'^product-detail/(?P<slug>[-\w]+)/$', product_detail, name = 'product_detail'),
]