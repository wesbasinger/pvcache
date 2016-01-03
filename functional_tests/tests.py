from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from cache.models import Geocache

class NewVisitorTest(LiveServerTestCase):

	def setUp(self):

		# bit of a hack, prepopulating the database
		first_listing = Geocache(
			title="First Geocache Listing",
			description="Test description",
			latitude=00.000000,
			longitude=00.000000,
			)
		first_listing.save()
		second_listing = Geocache(title="Second Geocache Listing")
		second_listing.save()

		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_view_index_page(self):

		# Cody has heard about a cool new online private 
		# geocaching app.
		# He goes to check out its homepage
		self.browser.get(self.live_server_url)

		# He notices the page title and header mention VT Caching
		self.assertIn('VT Caching', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('VT Caching', header_text)
		
		# He then is able to view listings for several different
		# geocaches in the area.  All listing are hyperlinks
		listings = self.browser.find_elements_by_tag_name('a')
		self.assertTrue(
			any( listing.text == 'First Geocache Listing' 
				for listing in listings)
		)
		self.assertTrue(
			any( listing.text == 'Second Geocache Listing' 
				for listing in listings)
		)
	def test_can_click_and_view_listing_detail(self):

		self.browser.get(self.live_server_url)
		# When he clicks on one of the listings, it shows all the
		# important information for that particular cache - which
		# includes a title, a description, latitude, 
		# longitude, and user logs.
		first_listing = self.browser.find_element_by_id('first').click()
		current_listing_url = self.browser.current_url
		self.assertRegex(current_listing_url, '/listing/.+')
		
		self.browser.find_element_by_id('title')
		self.browser.find_element_by_id('description')
		self.browser.find_element_by_id('latitude')
		self.browser.find_element_by_id('longitude')

		# The page lists all of the previous logs by other people
		# that have found the cache.
		self.browser.find_elements_by_tag_name('li')

		# He is also given the option to download the information
		# in a GPX file that can be imported to his device.

	def test_can_add_a_log_to_a_listing_and_view_later(self):

		# Once he finds the geocache, he is able to 
		# create a log entry.
		self.browser.get('http://localhost:8000/listing/3')
		inputbox = self.browser.find_element_by_id('id_new_log-input')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a new log'
		)

		# He types "New log" into a text box
		inputbox.send_keys('New log')

		# When he hits enter, the page updates, and now
		# it lists 'New log' as an item
		inputbox.send_keys(Keys.ENTER)
		
		log_entry = self.browser.find_element_by_id('id_new_log-output')
		self.assertEqual('New log', log_entry.text)

		# After he submits the log entry, the page 
		# refreshes and he is
		# able to see that his entry is the latest.
		
		# When Cody logs in as an admin user, he is able to add
		# geocaches of his own. 
