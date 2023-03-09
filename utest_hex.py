import unittest
from e_polygon import EquilateralPolygon
import math
from epolygon_hexagon import Hexagon



class TestHexagon(unittest.TestCase):

  
#REMOVING commented out lines in github for now

   # def length_and_width(self):
        #hexagon = Hexagon(5)
        #self.assertEqual(hexagon.GetLength(), 5)
        #self.assertEqual(hexagon.GetWidth(), 5)

    def test_area(self):
        hexagon = Hexagon(5)
        self.assertAlmostEqual(hexagon.GetArea(), 64.95, places=2)

    



if __name__ == '__main__':
    unittest.main()




#WORKING UTEST FOR CLASS HEXAGON


# class TestHexagon(unittest.TestCase):

#     def test_length_and_width(self):
#         hexagon = Hexagon(5)
#         self.assertEqual(hexagon.GetLength(), 5)
#         self.assertEqual(hexagon.GetWidth(), 5)

#     def test_area(self):
#         hexagon = Hexagon(5)
#         self.assertAlmostEqual(hexagon.GetArea(), 64.95, places=2)

#     def test_perimeter(self):
#         hexagon = Hexagon(5)
#         self.assertEqual(hexagon.GetPerimeter(), 30)

        

# if __name__ == '__main__':
#     unittest.main()
