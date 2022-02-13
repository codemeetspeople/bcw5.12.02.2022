import unittest
from point import Point


class TestPoint(unittest.TestCase):
    def test_constructor(self):
        a = Point()
        b = Point(10, 10)

        self.assertEqual(a.x, 0.0)
        self.assertEqual(a.y, 0.0)
        self.assertEqual(b.x, 10.0)
        self.assertEqual(b.y, 10.0)

    def test_str(self):
        a = Point()
        out = str(a)

        self.assertEqual(out, '(0.0, 0.0)')

    def test_operators(self):
        a = Point()
        b = Point(10, 10)

        self.assertTrue(a != b)
        self.assertFalse(a == b)
