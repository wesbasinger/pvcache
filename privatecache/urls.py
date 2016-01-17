"""privatecache URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.contrib import admin 
from cache import views
admin.autodiscover()

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
	url(r'^$', views.index, name="index"),
	url(r'^listing/(?P<geocache_id>[0-9]+)$', views.listing, name="listing"),
	url(r'^new$', views.new, name="new"),
	url(r'^about$', views.about, name="about"),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
	url(r'^newuser$', views.newuser, name="newuser"),
	url(r'gpx/(?P<geocache_id>[0-9]+)$', views.gpx, name="gpx"),
]
