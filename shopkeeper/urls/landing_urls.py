from django.conf.urls import url, include
from landing.views import user_homepage

urlpatterns = [
    url(r'^landing/', user_homepage, name = 'landing_homepage'),
    
]