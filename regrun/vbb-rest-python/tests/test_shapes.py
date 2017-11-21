from __future__ import print_function
import unittest

import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
module_path = os.path.abspath(os.path.join(here, os.pardir))
sys.path.insert(0, module_path)


class TestShapes(unittest.TestCase):
    @classmethod
    def setUp(cls):
        from vbb.client import VBBService
        cls.client = VBBService()
        cls.shapes = cls.client.shapes

    def test_get_shapes(self):
        shapes = self.shapes.get_shape(id=1269)
        self.assertEqual(len(shapes), 203)

    def test_get_shapes_type(self):
        shapes = self.shapes.get_shape(id=1269)
        shape = shapes[0]
        self.assertIsInstance(shape, list)
        print(shape)

    def test_get_shape(self):
        shapes = self.shapes.get_shape(id=1269)
        shape = shapes[0]
        self.assertItemsEqual(shape, [52.3849, 13.19434])

    def test_get_shape_type(self):
        shapes = self.shapes.get_shape(id=1269)
        shape = shapes[0][0]
        self.assertIsInstance(shape, int)
