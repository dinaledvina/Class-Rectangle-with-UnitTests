import unittest
import math
from rectangle import Rectangle
from circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.my_circle = Circle(5)

    def test_GetPerimeter(self):
    	self.assertEqual(self.my_circle.GetPerimeter(), 30)







if __name__ == '__main__':
    unittest.main()
