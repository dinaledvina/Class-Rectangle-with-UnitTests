import unittest
from rectangle import Rectangle
from hexagon import Hexagon



class TestHexagon(unittest.TestCase):

    def length_and_width(self):
        hexagon = Hexagon(5)
        self.assertEqual(hexagon.GetLength(), 5)
        self.assertEqual(hexagon.GetWidth(), 5)

    def test_area(self):
        hexagon = Hexagon(5)
        self.assertAlmostEqual(hexagon.GetArea(), 64.95, places=2)

    



if __name__ == '__main__':
    unittest.main()




