from circle import Circle
import unittest


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(5)

    def test_radius_type(self):
        self.assertIsInstance(self.c1.radius, (float, int), "Radius must be an integer or float type!")

    def test_radius_value(self):
        self.assertGreater(self.c1.radius, 0, "Radius must be greater than zero!")

    def test_exception_value(self):
        self.assertRaises(ValueError, self.c1.__init__, 0)

    def test_exception_type(self):
        with self.assertRaises(TypeError) as e:
            self.c1.__init__('f')
        self.assertEqual(str(e.exception), "Radius must be an integer or float type!")

    def test_length(self):
        self.assertEqual(self.c1.calc_len(), 31.41592653589793)

