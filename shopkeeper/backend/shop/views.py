from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Shop, ShopCategory
from .forms import ShopForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# def home()

def shop_list(request, shop_category_slug = None):
	shop_categories = ShopCategory.objects.all()
	shops_dict = {}
	if shop_category_slug != None:
		shop_list = Shop.objects.filter(category__slug = shop_category_slug).order_by('-added_on')
		shops_dict['shop_list'] = shop_list
		# print(context)
	else:
		shop_list = Shop.objects.all().order_by('-added_on')
		shops_dict['shop_list'] = shop_list

	context = {
		"shop_categories":shop_categories,
		"shops_dict":shops_dict,
	}
	# print(context)
	
	return render(request, 'shop/shop_list.html', context)


def shop_detail(request, slug = None):
	shop_instance = Shop.objects.filter(slug = slug).last()
	context = {
		"shop_instance":shop_instance
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
			# shop.cleaned_data.get('owner')
			# shop.cleaned_data.get('description')
			# shop.cleaned_data.get('name')
			# shop.cleaned_data.get('opening_date')
			# shop.cleaned_data.get('category')


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


# def shop_category_list(request):
# 	categories = ShopCategory.objects.all()
# 	context = {
# 		"categories":categories
# 	}
# 	return render(request, '')









