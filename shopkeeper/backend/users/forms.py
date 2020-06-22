from django import forms
from users.models import UserProfile

class RegistrationForm(forms.ModelForm):
	email = forms.EmailField(widget = forms.TextInput, label = 'email')
	password1 = forms.CharField(widget = forms.PasswordInput, label = 'password1')
	password2 = forms.CharField(widget = forms.PasswordInput, label = 'password2')

	class Meta:
		model = UserProfile
		fields = ('email',)

	def clean_email(self):
		email = self.cleaned_data.get('email')
		qs = UserProfile.objects.filter(email = email)
		if qs.exists():
			raise forms.ValidationError('Email already exists')
		return email

	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		if password1 and password2 and password1 != password2:
			raise forms.ValidationsError('Password doesnot match')
		return password2

	def save(self, commit = True):
		user = super(RegistrationForm, self).save(commit = False)
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
		return user


