from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestLocations(unittest.TestCase):
    @classmethod
    def setUp(cls):
        from vbb.client import VBBService
        cls.client = VBBService()
        cls.locations = cls.client.locations

    def test_get_locations(self):
        locations = self.locations.get_locations(query='Alexanderplatz')
        self.assertEqual(len(locations), 10)

    def test_get_location_attr(self):
        locations = self.locations.get_locations(query='Alexanderplatz')
        location = locations[0]
        self.assertIn('products', location)

    def test_get_location_routes(self):
        locations = self.locations.get_locations(query='Alexanderplatz')
        location = locations[0]['products']
        possibilities = location.keys()
        self.assertItemsEqual(possibilities, ['regional', 'tram', 'bus', 'suburban',
                                              'express', 'subway', 'ferry'])

    def test_get_location_route_by_ferry(self):
        locations = self.locations.get_locations(query='Alexanderplatz')
        ferry = locations[0]['products']['ferry']
        self.assertEqual(ferry, False)
