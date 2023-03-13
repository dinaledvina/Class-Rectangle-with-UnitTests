import unittest


class TestShape(unittest.TestCase):

    def test_shape_position(self):
        shape = Shape()
        shape.x = 0
        shape.y = 0
        self.assertEqual(shape.x, 0)
        self.assertEqual(shape.y, 0)
