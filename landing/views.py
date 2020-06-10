from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def home(request):
	return HttpResponse('<h1>This is home page1</h1>')
