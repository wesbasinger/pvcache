from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Geocache

def index(request):
	listings = Geocache.objects.all()
	return render(request, 'index.html', {'listings' : listings})

def listing(request, geocache_id):
	listing = get_object_or_404(Geocache, pk=geocache_id)
	logs = listing.log_set.all()
	return render(request, 'listing.html', {
		'listing': listing, 
		'log_text': request.POST.get('log_text', ''),
		'logs': logs})
