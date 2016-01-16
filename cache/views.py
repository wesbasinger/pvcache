from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Geocache, Log
from .forms import CacheForm

def index(request):
	listings = Geocache.objects.all()
	return render(request, 'index.html', {'listings' : listings})

def listing(request, geocache_id):
	if request.method == 'POST':
		listing = Geocache.objects.get(pk=geocache_id)
		new_log_text = request.POST['log_text']
		new_entry = Log(text=new_log_text, geocache=listing)
		new_entry.save()
		logs = listing.log_set.all()
		return render(request, 'listing.html', {
			'listing': listing,
			'logs': logs
		})
	listing = Geocache.objects.get(pk=geocache_id)
	logs = listing.log_set.all()
	return render(request, 'listing.html', {
			'listing': listing, 
			'logs': logs})

def new(request):
	if request.method == "POST":
		form = CacheForm(request.POST)
		if form.is_valid():
			geocache = form.save(commit=False)
			geocache.save()
			return HttpResponseRedirect('/')
	else:
		form = CacheForm()

	return render(request, 'new.html', {'form': form})

def about(request):
	return render(request, 'about.html', {})
