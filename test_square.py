import unittest
from polygon_square import Square

class TestSquare(unittest.TestCase):


    def test_area(self):
    	self.assertEqual(GetArea(), 25)

    def test_perimeter(self):
        self.assertEqual(GetPerimeter(), 20)





if __name__ == '__main__':
    unittest.main()
