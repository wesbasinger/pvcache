from django.shortcuts import render

from .models import Geocache

def index(request):
	listings = Geocache.objects.all()
	return render(request, 'index.html', {'listings' : listings}) 
