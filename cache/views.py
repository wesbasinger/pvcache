from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Geocache, Log
from .forms import CacheForm, NewUserForm

from xml.etree.ElementTree import Element, SubElement, Comment, tostring



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

@login_required
def delete(request, geocache_id):
	listing = Geocache.objects.get(pk=geocache_id)
	listing.delete()
	listings = Geocache.objects.all()
	return HttpResponseRedirect('/')
  

def newuser(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(
				username=request.POST['username'],
				password=request.POST['password']
			)
			new_user.save()
			return HttpResponseRedirect('/')
	else:
		form = NewUserForm()

	return render(request, 'newuser.html', {'form': form})


def about(request):
	return render(request, 'about.html', {})

def gpx(request, geocache_id):
	cache = get_object_or_404(Geocache, pk=geocache_id)

	root = Element('gpx')
	root.set('xmlns', 'http://ww.topografix.com/GPX/1/1')
	root.set('creator', 'Wes Basinger')
	root.set('version', '1.1')
	root.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
	root.set('xmlns:xsiSchemaLocation', 'http://www.togografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd')
	md = SubElement(root, 'metadata')
	nm = SubElement(md, 'name')
	nm.text = cache.title
	ds = SubElement(md, 'description')
	ds.text = cache.description
	wpt = SubElement(root, 'wpt')
	wpt.set('lat', str(cache.latitude))
	wpt.set('lon', str(cache.longitude))
	bounds = SubElement(root, 'bounds')
	bounds.set('minlat', str(cache.latitude))
	bounds.set('minlon', str(cache.longitude))
	bounds.set('maxlat', str(cache.latitude))
	bounds.set('maxlon', str(cache.longitude))
	nr = SubElement(wpt, 'name')
	nr.text = "VT Cache" 
	sy = SubElement(wpt, 'sym')
	sy.text = 'Waypoint'
	str_output = tostring(root)

	response = HttpResponse(str_output, content_type='text/xml')
	response['Content-Disposition'] = 'attachment; filename="%s.gpx"' % cache.title
	
	return response
