import unittest


class TestShape(unittest.TestCase):

    def test_shape_position(self):
        shape = Shape()
        self.assertEqual(shape.x, 0)
        self.assertEqual(shape.y, 0)
