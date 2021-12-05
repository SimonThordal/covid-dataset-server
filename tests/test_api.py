import unittest
import hug
from .context import api


class TestApi(unittest.TestCase):
    def test_initial_route(self):
        result = hug.test.get(api, "hello_world")
        self.assertEqual(result.status, hug.HTTP_200)

    def test_rolling_endpoint(self):
        # When calling the endpoint with a valid country code
        code = "ESP"
        result = hug.test.get(api, "/rolling-five-days/{}".format(code))
        # The request is succesful
        self.assertEqual(result.status, hug.HTTP_200)
        # The response is JSON
        self.assertEqual(result.headers_dict['content-type'], 'application/json; charset=utf-8')
        # The response contains data for the given country
        self.assertIn('counts', result.data)
        self.assertGreater(len(result.data['counts']), 0)
        # The response contains the expected keys
        self.assertIn('country', result.data)
        self.assertEqual('Spain', result.data['country'])
        self.assertIn('country_code', result.data)
        self.assertEqual('ESP', result.data['country_code'])
