import unittest


class TestShape(unittest.TestCase):

    def test_shape_position(self):
        shape = Shape()


        set_position(shape.x, shape.y)
       
        self.assertEqual(get_position(), (shape.x, shape.y))
        
        
        

