from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from cache.models import Geocache, Log
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


class ListingTest(TestCase):

	def test_listing_returns_correct_html(self):
		cache = Geocache.objects.create()
		request = HttpRequest()
		response = listing(request, cache.id)
		expected_html = render_to_string(
			'listing.html',
			{'listing': listing}
		)
		self.assertIsNotNone(response.content.decode())

	def test_listing_page_can_save_a_POST_request(self):
		cache = Geocache.objects.create()
		cache.save()
		old_log = Log(text='An old log', geocache=cache)
		old_log.save()
		request = HttpRequest()
		request.method = 'POST'
		request.POST['log_text'] = 'A new log'

		response = listing(request, cache.id)
		
		self.assertEqual(Log.objects.count(), 2)

		self.assertIn('A new log', response.content.decode())
		self.assertIn('An old log', response.content.decode())

	def test_all_previous_logs_are_shown(self):
		g = Geocache()
		g.save()
		first_log = Log(id=None, text="Test for first log", geocache=g)
		first_log.save()
		second_log = Log(id=None, text="Test for second log", geocache=g)
		second_log.save()
		request = HttpRequest()
		
		response = listing(request, g.id)

		self.assertIn("Test for first log", response.content.decode())
		self.assertIn("Test for second log", response.content.decode())
		
		

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

	def test_can_covert_decimal_coordinates_to_DMS(self):
		g = Geocache(latitude=32.603020, longitude=96.863314)
		self.assertEqual(
			g.dms(), "N 32 36' 10.872\" W 96 51' 47.93\""
		)

	def test_saving_and_retrieving_hint(self):
		first_listing = Geocache()
		first_listing.hint = "Hint for cache"
		first_listing.save()

		second_listing = Geocache()
		second_listing.hint = "Hint for cache"
		second_listing.save()

		saved_listings = Geocache.objects.all()
		self.assertEqual(saved_listings.count(), 2)

		first_saved_listing = saved_listings[0]
		second_saved_listing = saved_listings[1]
		self.assertEqual(first_saved_listing.hint, "Hint for cache")
		self.assertEqual(second_saved_listing.hint, "Hint for cache")

class LogModeltest(TestCase):

	def test_geocache_and_log_relationship(self):
		g = Geocache()
		g.save()
		log = Log(id=None, text="test text", geocache=g)
		log.save()
		self.assertEqual(log.text, "test text")
		log2 = Log(id=None, text="test text", geocache=g)
		log2.save()
		saved_logs = Log.objects.all()
		self.assertEqual(saved_logs.count(), 2)
