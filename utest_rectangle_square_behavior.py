import unittest
from rectangle import Rectangle
from square import Square

class TestSquare(unittest.TestCase):
    def test_same_behavior_as_rectangle(self):
        rect = Rectangle(5, 10)
        square = Square(5)

        self.assertEqual(rect.GetLength(), square.GetLength())
        self.assertEqual(rect.GetWidth(), square.GetWidth())
        self.assertEqual(rect.GetArea(), square.GetArea())
        self.assertEqual(rect.GetPerimeter(), square.GetPerimeter())


if __name__ == '__main__':
    unittest.main()








