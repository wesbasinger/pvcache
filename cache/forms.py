from django.forms import ModelForm
from .models import Geocache
from django.contrib.auth.models import User

class CacheForm(ModelForm):

	class Meta:
		model = Geocache
		fields = [ 
			'title',
			'description',
			'latitude',
			'longitude',
			'hint',
			'difficulty',
		]

class NewUserForm(ModelForm):

	class Meta:
		model = User
		fields = [
			'username',
			'password',
			'email',
			'first_name',
			'last_name',
		]
