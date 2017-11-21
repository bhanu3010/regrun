from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)
from requests import Response


class TestLocations(unittest.TestCase):
    @classmethod
    def setUp(cls):
        from vbb.client import VBBService
        cls.client = VBBService()
        cls.lines = cls.client.lines

    def test_get_line(self):
        line = self.lines.get_line(_id='5232_3')
        self.assertIsInstance(line, dict)

    def test_get_line_product(self):
        line = self.lines.get_line(_id='5232_3')
        self.assertEqual(line['product'], 'bus')

    def test_get_line_mode(self):
        line = self.lines.get_line(_id='5232_3')
        self.assertEqual(line['mode'], 'bus')

    def test_get_line_operator(self):
        line = self.lines.get_line(_id='5232_3')
        self.assertEqual(line['operator'], u'32')

    def test_get_lines(self):
        line = self.lines.get_lines(operator=796)
        self.assertIsInstance(line, Response)
