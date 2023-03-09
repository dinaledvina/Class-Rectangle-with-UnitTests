import unittest
from polygon_hexagon import Hexagon



class TestHexagon(unittest.TestCase):

  


    def test_area(self):
       
        self.assertAlmostEqual(GetArea(), 64.95, places=2)

    



if __name__ == '__main__':
    unittest.main()






