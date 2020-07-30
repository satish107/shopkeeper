from django.db import models
from users.models import UserProfile
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class ProductCategory(models.Model):
	name = models.CharField(max_length = 255, null = True, blank = True, db_index = True)
	slug = models.SlugField(null = True, blank = True, db_index = True, unique = True)
	added_on = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updated_on = models.DateTimeField(auto_now = True, null = True, blank = True)

	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'Product Categories'

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(ProductCategory, self).save(*args, **kwargs)


class Product(models.Model):
	category = models.ForeignKey(ProductCategory, on_delete = models.CASCADE, related_name = 'products')
	name = models.CharField(max_length = 255, null = True, blank = True)
	slug = models.SlugField(null = True, blank = True, unique = True)
	image = models.ImageField(upload_to = 'images/shop/products/', null = True, blank = True)
	description = models.TextField(null = True, blank = True)
	price = models.DecimalField(max_digits = 10, decimal_places = 2, null = True, blank = True)
	stock = models.PositiveIntegerField(null = True, blank = True)
	available = models.BooleanField(default = True)
	added_on = models.DateTimeField(auto_now_add = True, null = True, blank = True)
	updated_on = models.DateTimeField(auto_now = True, null = True, blank = True)

	class Meta:
		ordering = ('name',)
		# index_together = (('id', 'slug'),)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(Product, self).save(*args, **kwargs)