from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestRadar(unittest.TestCase):
    @classmethod
    def setUp(cls):
        from vbb.client import VBBService
        cls.client = VBBService()
        cls.radar = cls.client.radar

    def test_get_radar(self):
        radar = self.radar.get_radar(north=52.52411, west=13.41002, south=52.51942, east=13.41709)
        self.assertIsInstance(radar, list)

    def test_get_radar_attr(self):
        radar = self.radar.get_radar(north=52.52411, west=13.41002, south=52.51942, east=13.41709)[0]
        self.assertIn('frames', radar)

    def test_get_radar_frames(self):
        radar = self.radar.get_radar(north=52.52411, west=13.41002, south=52.51942, east=13.41709)[0]
        self.assertIsInstance(radar['frames'], list)

    def test_get_possible_routes(self):
        radar = self.radar.get_radar(north=52.52411, west=13.41002, south=52.51942, east=13.41709)[0]
        routes = radar['frames'][0]['origin']['products'].keys()
        self.assertItemsEqual(routes, ['regional', 'tram', 'bus', 'suburban', 'express', 'subway', 'ferry'])