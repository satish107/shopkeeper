from django.conf.urls import url, include
from users.views import register, login_user, logout_user

urlpatterns = [
    url(r'^register/', register, name = 'register'),
    url(r'^login', login_user, name = 'login_user'),
    url(r'^logout', logout_user, name = 'logout_user'),
    
]