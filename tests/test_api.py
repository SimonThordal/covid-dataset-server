import unittest
import hug
from .context import api

class TestApi(unittest.TestCase):
	def test_initial_route(self):
		result = hug.test.get(api, "hello_world")
		self.assertEqual(result.status, hug.HTTP_200)

	def test_rolling_endpoint(self):
		code = "es"
		result = hug.test.get(api, "/rolling-five-days/{}".format(code))
		self.assertEqual(result.status, hug.HTTP_200)