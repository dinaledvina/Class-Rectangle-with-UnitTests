
import unittest
from rectangle import Rectangle

class RectangleTest(unittest.TestCase):
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
        
        
        
    def test_set_length(self):
        self.rectangle.set_length(7)
        self.assertEqual(self.rectangle.length, 7)
        
        self.assertEqual(self.rectangle.corners, ((0,0), (7, 0), (7, 10), (0, 10)))
        
    def test_set_width(self):
        self.rectangle.set_width(12)
        self.assertEqual(self.rectangle.width, 12)
        
        self.assertEqual(self.rectangle.corners, ((0,0), (5, 0), (5, 12), (0, 12)))
        
        
        

    def test_set_corners(self):
        
        self.rect.set_corners((0,0), (7,12))
        self.assertEqual(self.rect.get_corners(), ((0,0), (7,0), (7,12), (0,12)))
        self.assertEqual(self.rect.GetLength(), 7)
        self.assertEqual(self.rect.GetWidth(), 12)





if __name__ == '__main__':
    unittest.main()
