from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestRadar(unittest.TestCase):
    @staticmethod
    def do_init():
        from vbb.client import VBBService
        client = VBBService()
        return client

    def test_get_radar(self):
        client = self.do_init()
        shape = client.shapes.get_shape(id=1269)
#        print(shape)
