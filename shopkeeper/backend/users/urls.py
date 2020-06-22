from django.conf.urls import url, include
from users.views import register_user
app_name = 'users'
urlpatterns = [
    url(r'^$', register_user, name = 'register_user'),
    
]