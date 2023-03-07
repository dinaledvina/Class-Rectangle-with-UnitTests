# import unittest
# from rectangle import Rectangle

# class TestRectangle(unittest.TestCase):

#     def setUp(self):
#         self.rectangle = Rectangle()
#         self.rectangle.length = 5
#         self.rectangle.width = 10

#     def test_GetLength(self):
#         self.assertEqual(self.rectangle.GetLength(), 5)

#     def test_GetWidth(self):
#         self.assertEqual(self.rectangle.GetWidth(), 10)

#     def test_GetArea(self):
#         self.assertEqual(self.rectangle.GetArea(), 50)

#     def test_GetPerimeter(self):
#         self.assertEqual(self.rectangle.GetPerimeter(), 30)

# if __name__ == '__main__':
#     unittest.main()






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

if __name__ == '__main__':
    unittest.main()
