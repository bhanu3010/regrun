from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestStations(unittest.TestCase):

    @classmethod
    def setUp(self):
        from vbb.client import VBBService
        self.client = VBBService()

    def test_get_station(self):
        station = self.client.stations.get_station_by_id(id=900000013102)
        self.assertIsInstance(station, dict)

    def test_get_nearby_stations(self):
        station = self.client.stations.get_nearby_stations(latitude=52.52725, longitude=13.4123)
        self.assertIsNotNone(station)

    def test_get_station_departures(self):
        station = self.client.stations.get_station_departures(id=900000013102)
        self.assertIsNotNone(station)

    def test_get_all_stations(self):
        stations = self.client.stations.get_all_stations()
        self.assertEqual(len(stations), 13098)