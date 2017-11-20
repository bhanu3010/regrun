from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)

from vbb.client import VBBService


class TestJourneys(unittest.TestCase):
    @staticmethod
    def do_init():
        client = VBBService()
        return client

    def test_get_journeys(self):
        client = self.do_init()
        journeys = client.journeys.get_journeys(_from='900000017104', _to='900000017101')

