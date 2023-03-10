import unittest
from e_polygon import EquilateralPolygon
from epolygon_hexagon import Hexagon



class TestHexagon(unittest.TestCase):


    def test_area(self):
        
        self.assertAlmostEqual(hexagon.GetArea(), 64.95, places=2)

    

hexagon = Hexagon(6, 5)

if __name__ == '__main__':
    unittest.main()






