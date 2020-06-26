from django.shortcuts import render

# Create your views here.

def user_homepage(request):
	return render(request, 'landing/main/base.html')