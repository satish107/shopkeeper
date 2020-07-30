from django.db import models
from users.models import UserProfile
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class ShopCategory(models.Model):
	name = models.CharField(max_length = 255, null = True, blank = True)
	slug = models.SlugField(null = True, blank = True)
	image = models.ImageField(upload_to = 'images/shop_category/', null = True, blank = True)
	description = models.TextField(null = True, blank = True)
	added_on = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updated_on = models.DateTimeField(auto_now = True, null = True, blank = True)

	class Meta:
		ordering = ('-added_on',)
		verbose_name_plural = 'Shop Categories'

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(ShopCategory, self).save(*args, **kwargs)

	# def get_absolute_url(self):
	# 	return reverse('shop:shop_list_category', args = [str(self.slug)])


class Shop(models.Model):
	name = models.CharField(max_length = 255, null = True, blank = True)
	slug = models.SlugField(null = True, blank = True)
	owner = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
	address = models.CharField(max_length = 255, null = True, blank = True)
	image = models.ImageField(upload_to = 'images/shop/', null = True, blank = True)
	description = models.TextField(null = True, blank = True)
	category = models.ManyToManyField(ShopCategory, blank = True)
	opening_date = models.DateTimeField(null = True, blank = True)
	added_on = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updated_on = models.DateTimeField(auto_now = True, null = True, blank = True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Shop, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('shop:shop_detail', args = [str(self.slug)])











	

