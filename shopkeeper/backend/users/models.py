from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserProfileManager(BaseUserManager):

	def create_user(self, email, name, username, password = None):
		if not email:
			raise ValueError("User must have email address")

		user = self.model(
				name = name,
				username = username,
				email = self.normalize_email(email),
			)
		user.set_password(password)
		user.save(using = self._db)

		return user

	def create_superuser(self, email, name, username, password):
		if not email:
			raise ValueError("User must have email address")

		user = self.create_user(
				name = name,
				username = username,
				email = email,
				password = password
			)

		user.is_superuser = True
		user.is_admin = True
		user.is_staff = True
		user.save(using = self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(max_length = 255, null = True, blank = True, unique = True)
	name = models.CharField(max_length = 255, null = True, blank = True)
	username = models.CharField(max_length = 255, null = True, blank = True)
	is_staff = models.BooleanField(default = False)
	is_admin = models.BooleanField(default = False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username', 'name']

	objects = UserProfileManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		# user is identified by email
		return self.email

	def get_short_name(self):
		# user is identified by email
		return self.email

