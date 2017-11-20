from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestStations(unittest.TestCase):

    @staticmethod
    def do_init():
        from vbb.client import VBBService
        client = VBBService()
        return client

    def test_get_station(self):
        client = self.do_init()
        station = client.stations.get_station_by_id(id=900000013102)
#        print(station)

    def test_get_nearby_stations(self):
        client = self.do_init()
        station = client.stations.get_nearby_stations(latitude=52.52725, longitude=13.4123)
 #       print(station)

    def test_get_station_departures(self):
        client = self.do_init()
        station = client.stations.get_station_departures(id=900000013102)
      #  assert 1 is None
  #      print(station)

    def test_get_all_stations(self):
        client = self.do_init()
        stations = client.stations.get_all_stations()
   #     print(stations)
