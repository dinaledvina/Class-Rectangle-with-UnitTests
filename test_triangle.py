import unittest

class TestTriangle(unittest.TestCase):
    def test_area(self):
        t = Triangle(3, 4, 5)
        self.assertEqual(t.area(), 6.0)

if __name__ == '__main__':
    unittest.main()
