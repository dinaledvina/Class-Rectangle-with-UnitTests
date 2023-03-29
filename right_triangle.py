

class RightTriangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.corners = ((0,0), (self.a, 0), (0, self.b))

    def perimeter(self):
    	return (self.a + self.b + self.c)

    def area(self):
    	s = (self.a + self.b + self.c) / 2
    	return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5


    def set_corners(self, corner1, corner2, corner3):
        self.corners = (corner1, corner2, corner3)

    def get_corners(self):
        return self.corners

    def set_length(self, a_l, b_l, c_l):
    	self.a = a_l
    	self.b = b_l
    	self.c = c_l
    	self.corners = ((0,0), (self.a, 0), (0, self.b))