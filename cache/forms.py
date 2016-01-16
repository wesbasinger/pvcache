from django.forms import ModelForm
from .models import Geocache

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

