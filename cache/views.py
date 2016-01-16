from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Geocache, Log
from .forms import CacheForm, NewUserForm

def index(request):
	listings = Geocache.objects.all()
	return render(request, 'index.html', {'listings' : listings})

def listing(request, geocache_id):
	if request.method == 'POST':
		listing = Geocache.objects.get(pk=geocache_id)
		new_log_text = request.POST['log_text']
		username = request.user.username
		new_entry = Log(text=new_log_text, geocache=listing, author=username)
		new_entry.save()
		logs = listing.log_set.all().order_by('-id')
		return render(request, 'listing.html', {
			'listing': listing,
			'logs': logs,
		})
	listing = Geocache.objects.get(pk=geocache_id)
	logs = listing.log_set.all().order_by('-id')
	return render(request, 'listing.html', {
			'listing': listing, 
			'logs': logs})

@login_required
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

def newuser(request):
	if request.method == "POST":
		form =NewUserForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.save()
			return HttpResponseRedirect('/')
	else:
		form = NewUserForm()

	return render(request, 'newuser.html', {'form': form})


def about(request):
	return render(request, 'about.html', {})
