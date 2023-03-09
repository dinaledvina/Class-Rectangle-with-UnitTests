import unittest
from e_polygon import EquilateralPolygon
import math
from epolygon_square import Square

class TestSquare(unittest.TestCase):


    def test_area(self):
    	self.assertEqual(square.GetArea(), 25)

    def test_perimeter(self):
        self.assertEqual(square.GetPerimeter(), 20)



square = Square(4)

if __name__ == '__main__':
    unittest.main()