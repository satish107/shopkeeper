from django.shortcuts import render
from users.models import UserProfile
from users.forms import RegistrationForm
# Create your views here.

def register_user(request):
	if request.method == "POST":
		registration_form = RegistrationForm(request.POST)
		if registration_form.is_valid():
			registration_form.save()
	else:
		registration_form = RegistrationForm()

	
	context = {
		'registration_form':registration_form
	}
	return render(request, 'users/username.html', context)

