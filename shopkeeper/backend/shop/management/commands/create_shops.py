from django.core.management.base import BaseCommand
from django.utils import timezone
from shop.models import Shop, ShopCategory
from users.models import UserProfile
from model_mommy import mommy
import names
import random
from datetime import datetime
class Command(BaseCommand):
	help = "command for creating shops in bulk"

	def add_arguments(self, parser):
		parser.add_argument('count', nargs=1, type=int)


	def handle(self, *args, **options):
		self.clear()
		self.make_shops(options)
		self.connect_categories()

	def make_shops(self, options):
		self.shops = []
		for i in range(options.get('count')[0]):
			shop_object = mommy.prepare(
					Shop,
					name = "shop %d"%(i),
					owner = random.choice(UserProfile.objects.all()),
					address = "Address of shop %d"%(i),
					description = "Description for shop %d"%(i),
					category = ShopCategory.objects.all(),
					opening_date = timezone.now()
				)
			self.shops.append(shop_object)
		Shop.objects.bulk_create(self.shops)

	def connect_categories(self):
		for shop in Shop.objects.all():
			random_categories = random.sample(list(ShopCategory.objects.all()), random.randint(1, 5))
			shop.image = "images/shop/shop-building-colorful-isolated-white-33822015.jpg"
			for j in random_categories:
				shop.category.add(j)
				shop.save()

	def clear(self):
		Shop.objects.all().delete()
		# ShopCategory.objects.all().delete()

