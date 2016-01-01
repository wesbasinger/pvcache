from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_view_index_page(self):

		# Cody has heard about a cool new online private 
		# geocaching app.
		# He goes to check out its homepage
		self.browser.get('http://localhost:8000')

		# He notices the page title and header mention VT Caching
		self.assertIn('VT Caching', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('VT Caching', header_text)

		# He then is able to view listings for several different
		# geocaches in the area.
		listings = self.browser.find_elements_by_tag_name('h2')
		self.assertTrue(
			any( listing.text == 'First Geocache Listing' 
				for listing in listings)
		)
		self.assertTrue(
			any( listing.text == 'Second Geocache Listing' 
				for listing in listings)
		)
	

		# When he clicks on one of the listings, it shows all the
		# important information for that particular cache - which
		# includes a title, a description, latitude, 
		# longitude, and user logs.

		# He is also given the option to download the information
		# in a GPX file that can be imported to his device.

		# Once he finds the geocache, he is able to 
		# create a log entry.

		# After he submits the log entry, the page 
		# refreshes and he is
		# able to see that his entry is the latest.

		# When Cody logs in as an admin user, he is able to add
		# geocaches of his own. 

if __name__ == '__main__':
	unittest.main(warnings='ignore')
