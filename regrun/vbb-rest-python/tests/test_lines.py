from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestLocations(unittest.TestCase):
    @staticmethod
    def do_init():
        from vbb.client import VBBService
        client = VBBService()
        return client

    def test_get_line(self):
        client = self.do_init()
        line = client.lines.get_line(_id='5232_3')
  #      print(line)

    def test_get_lines(self):
        client = self.do_init()
        line = client.lines.get_lines(operator=796)
   #     print(line)
