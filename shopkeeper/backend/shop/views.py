from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from shop.models import Shop, ShopCategory
from shop.forms import ShopForm
from product.models import ProductCategory, Product

# Create your views here.

def shop_list(request, shop_category_slug = None):
	shop_categories = ShopCategory.objects.all()
	shops_dict = {}
	if shop_category_slug != None:
		shop_list = Shop.objects.filter(category__slug = shop_category_slug).order_by('-added_on')
		shops_dict['shop_list'] = shop_list
	else:
		shop_list = Shop.objects.all().order_by('-added_on')
		shops_dict['shop_list'] = shop_list

	context = {
		"shop_categories":shop_categories,
		"shops_dict":shops_dict,
	}
	
	return render(request, 'shop/shop_list.html', context)


def shop_detail(request, slug = None):
	shop_instance = Shop.objects.filter(slug = slug).last()
	shop_category = shop_instance.category.all().values_list('name', flat = True)
	shop_category = ", ".join(shop_category)
	products = Product.objects.all()
	# if product_category_slug is not None:
	# 	products = products.filter(slug = product_category_slug)

	shop_categories = ShopCategory.objects.all()

	context = {
		"shop_instance":shop_instance,
		"shop_category":shop_category,
		"products":products,
		"shop_categories":shop_categories
	}
	return render(request, 'shop/shop_detail.html', context)


@login_required(login_url = 'users:login_user')
def shop_create(request):
	if request.method == "POST":
		form = ShopForm(request.POST, request.FILES)
		print('before form valid')
		print(request.POST['category'])
		if form.is_valid():
			shop = form.save(commit = False)
			shop.owner = request.user
			shop.save()
			form.save_m2m()
			return redirect('/')
		return HttpResponse('form is not valid')
	else:
		form = ShopForm()

	shop_categories = ShopCategory.objects.all().order_by('-added_on')

	context = {
		"form":form,
		"shop_categories":shop_categories
	}
	return render(request, 'shop/shop_create.html', context)


def shop_edit(request, slug = None):
	shop_instance = Shop.objects.filter(slug = slug).last()
	if request.method == "POST":
		form = ShopForm(request.POST, request.FILES, instance = shop_instance)
		if form.is_valid():
			shop = form.save(commit = False)
			shop.owner = request.user
			shop.save()
			return 
	else:
		form = ShopForm(instance = shop_instance)
	context = {
		"form":form,
		"shop_instance":shop_instance,
	}
	return render(request, 'shop/shop_edit.html', context)






