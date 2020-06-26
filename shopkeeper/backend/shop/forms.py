from django import forms
from .models import Shop


class ShopForm(forms.ModelForm):

	class Meta:
		model = Shop
		fields = ('name', 'address', 'image', 'description', 'category', 'opening_date')

