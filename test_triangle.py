import unittest

class TestTriangle(unittest.TestCase):
    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.area(), 6.0)

    # def test_is_equilateral(self):
    #     t = Triangle(5, 5, 5)
    #     self.assertTrue(t.is_equilateral())

    #     t = Triangle(3, 4, 5)
    #     self.assertFalse(t.is_equilateral())

    # def test_is_isosceles(self):
    #     t = Triangle(5, 5, 3)
    #     self.assertTrue(t.is_isosceles())

    #     t = Triangle(3, 4, 5)
    #     self.assertFalse(t.is_isosceles())

if __name__ == '__main__':
    unittest.main()
