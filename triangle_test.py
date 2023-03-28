import unittest

class TriangleTest(unittest.TestCase):
    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.area(), 6.0)
        
    def test_perimeter(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.perimeter(), 12)

   def test_set_corners(self):
        t = Triangle(4, 3, 5)
        t.set_corners((0,0), (4,0), (0, 3))
        self.assertEqual(t.get_corners(), ((0,0), (4,0), (0, 3)))
        self.assertEqual(t.a, 4)
        self.assertEqual(t.b, 3)
        self.assertEqual(t.c, 5)



    def test_set_length(self):
        t = Triangle(0, 0, 0)
        t.set_length(6, 8, 10)
        self.assertEqual(t.a, 6)
        self.assertEqual(t.b, 8)
        self.assertEqual(t.c, 10)

        expected_corners = ((0,0), (6,0), (0,8))

if __name__ == '__main__':
    unittest.main()
