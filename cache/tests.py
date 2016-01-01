from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from cache.views import index

class IndexTest(TestCase):

	def test_root_url_resolves_to_index_view(self):
		found = resolve('/')
		self.assertEqual(found.func, index)

	def test_index_returns_correct_html(self):
		request = HttpRequest()
		response = index(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>VT Caching</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))
