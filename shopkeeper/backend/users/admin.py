from django.contrib import admin
from .models import UserProfile

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ['email', 'name', 'username', 'is_staff', 'is_admin']

admin.site.register(UserProfile, UserProfileAdmin)