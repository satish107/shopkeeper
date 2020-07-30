from django.shortcuts import render, get_object_or_404
from product.models import Product, ProductCategory

# Create your views here.

def product_list(request, category_slug = None):
	product_category = None
	product_categories = ProductCategory.objects.all()
	products = Product.objects.filter(available = True)
	if category_slug:
		product_category = get_object_or_404(ProductCategory, slug = category_slug)
		products = products.filter(category = product_category)

	context = {
		"product_categories": product_categories,
		"products": products,
		"product_category":product_category,
	}
	return render(request, 'product/product_list.html', context)


def product_detail(request, slug = None):
	product_instance = get_object_or_404(Product, slug = slug)

	context = {
		"product_instance": product_instance
	}
	return render(request, 'product/product_detail.html', context)