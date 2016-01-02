from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from cache.models import Geocache
from cache.views import index, listing

class IndexTest(TestCase):

	def test_root_url_resolves_to_index_view(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_index_returns_correct_html(self):
		request = HttpRequest()
		response = index(request)
		expected_html = render_to_string('index.html')
		self.assertEqual(response.content.decode(), expected_html)


class GeocacheModeltest(TestCase):

	def test_saving_and_retrieving_items(self):
		first_listing = Geocache()
		first_listing.title = "First Geocache Listing"
		first_listing.description = "First geocache description."
		first_listing.save()

		second_listing = Geocache()
		second_listing.title = "Second Geocache Listing"
		second_listing.description = "Second geocache description."
		second_listing.save()

		saved_listings = Geocache.objects.all()
		self.assertEqual(saved_listings.count(), 2)

		first_saved_listing = saved_listings[0]
		second_saved_listing = saved_listings[1]
		self.assertEqual(first_saved_listing.title, "First Geocache Listing")
		self.assertEqual(first_saved_listing.description, "First geocache description.")
		self.assertEqual(second_saved_listing.title, "Second Geocache Listing")
		self.assertEqual(second_saved_listing.description, "Second geocache description.")

	def test_saving_and_retrieving_positive_and_negative_coordinates(self):
		first_listing = Geocache()
		first_listing.latitude = 10.000001
		first_listing.longitude = -10.000001
		first_listing.save()

		second_listing = Geocache()
		second_listing.latitude = 20.100000
		second_listing.longitude = -20.100000
		second_listing.save()

		saved_listings = Geocache.objects.all()
		self.assertEqual(saved_listings.count(), 2)

		first_saved_listing = saved_listings[0]
		second_saved_listing = saved_listings[1]
		self.assertEqual(first_saved_listing.latitude, 10.000001)
		self.assertEqual(first_saved_listing.longitude, -10.000001)
		self.assertEqual(second_saved_listing.latitude, 20.100000)
		self.assertEqual(second_saved_listing.longitude, -20.100000)

