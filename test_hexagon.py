import unittest
from hexagon import Hexagon


class TestHexagon(unittest.TestCase):

    def test_area(self):
        hexagon = Hexagon(6, 5)
        self.assertAlmostEqual(hexagon.GetArea(), 64.95, places=2)

    def test_perimeter(self):
        hexagon = Hexagon(6, 5)
        self.assertEqual(hexagon.GetPerimeter(),30)

if __name__ == '__main__':
    unittest.main()






