from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side_length):
        self.side_length = side_length
        self.corners = ((0,0), (self.side_length, 0), (self.side_length, self.side_length), (0, self.side_length))
        super().__init__(side_length, side_length)












