from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)

from vbb.client import VBBService


class TestJourneys(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.client = VBBService()
        cls.journeys = cls.client.journeys
        # journeys init per function helps in interleaved execution of tests.

    def test_get_total_journeys(self):
        journeys = self.journeys.get_journeys(_from='900000017104', _to='900000017101')
        self.assertEqual(len(journeys), 6)

    def test_get_journey_type(self):
        journeys = self.journeys.get_journeys(_from='900000017104', _to='900000017101')
        self.assertIsInstance(journeys[0], dict)

    def test_journey_origin_attr(self):
        journeys = self.journeys.get_journeys(_from='900000017104', _to='900000017101')
        journey = journeys[0]
        self.assertIn('origin', journey)

    def test_journey_origin_attr_value(self):
        journeys = self.journeys.get_journeys(_from='900000017104', _to='900000017101')
        journey_origin = journeys[0]['origin']
        self.assertIsInstance(journey_origin, dict)

    def test_journey_origin_type(self):
        journeys = self.journeys.get_journeys(_from='900000017104', _to='900000017101')
        origin_type = journeys[0]['origin']['type']
        self.assertIn(origin_type, 'station')


