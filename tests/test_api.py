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
        counts = result.data['counts']
        self.assertEqual(len(counts), 5)
        # The response contains the expected keys
        self.assertIn('country_code', result.data)
        self.assertEqual('esp', result.data['country_code'])

    def test_totals_endpoint(self):
        # When getting the totals endpoint
        result = hug.test.get(api, "/total-data")
        # The result is an object with country code keys
        self.assertIn('esp', result.data)
        # And integer sums
        [self.assertIsInstance(v, int) for _, v in result.data.items()]
        
