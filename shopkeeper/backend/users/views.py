from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from users.models import UserProfile
from users.forms import RegistrationForm, AuthenticationForm

# Create your views here.

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password1 = request.POST['password1']
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = RegistrationForm()
	context = {
		'form':form
	}
	return render(request, 'users/base.html', context)


def login_user(request):
	if request.method == "POST":
		form = AuthenticationForm(request.POST)
		if form.is_valid():
			email = request.POST['email']
			password = request.POST['password']
			user = authenticate(request, email = email, password = password)
			if user is not None:
				login(request, user)
				return redirect('/')
			return HttpResponse('You are not registered or check your email and password again')
	else:
		form = AuthenticationForm()
	context = {
		'form':form
	}
	return render(request, 'users/login.html', context)


def logout_user(request):
	logout(request)
	return redirect('/')
