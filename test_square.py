import unittest
from polygon import EquilateralPolygon
import math
from polygon_square import Square

class TestSquare(unittest.TestCase):


    def test_area(self):
        square = Square(4)
    	self.assertEqual(square.GetArea(), 25)

    def test_perimeter(self):
        square = Square(4)
        self.assertEqual(square.GetPerimeter(), 20)





if __name__ == '__main__':
    unittest.main()
