
import unittest
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rect = Rectangle(5, 10)
    
    def test_GetLength(self):
        self.assertEqual(self.rect.GetLength(), 5)
    
    def test_GetWidth(self):
        self.assertEqual(self.rect.GetWidth(), 10)
    
    def test_GetArea(self):
        self.assertEqual(self.rect.GetArea(), 50)
    
    def test_GetPerimeter(self):
        self.assertEqual(self.rect.GetPerimeter(), 30)


    def test_set_get_corners(self):
        
        self.assertEqual(self.rect.get_corners(), ((0, 0), (5, 10)))



if __name__ == '__main__':
    unittest.main()
