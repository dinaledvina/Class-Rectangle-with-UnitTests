import unittest
from rectangle import Rectangle
from right_triangle import RightTriangle



class TestRightTriangle(unittest.TestCase):
    def test_same_behavior_as_rectangle(self):
        rect = Rectangle(5, 10)
        rt = RightTriangle(3, 4)
    
        self.assertEqual(rect.GetLength(), rt.GetLength())
        self.assertEqual(rect.GetWidth(), rt.GetWidth())
        self.assertEqual(rect.GetArea(), rt.GetArea())
        self.assertEqual(rect.GetPerimeter(), rt.GetPerimeter())


if __name__ == '__main__':
    unittest.main()




