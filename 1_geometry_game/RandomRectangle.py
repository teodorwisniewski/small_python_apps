from RandomPoint import RandomPoint


class RandomRectangle:

    def __init__(self):
        self.bottom_left_pnt = RandomPoint()
        self.upper_right_pnt = RandomPoint(min_x=self.bottom_left_pnt.x,
                                     min_y=self.bottom_left_pnt.y)

    def __repr__(self):
        return f"Rectangle Coordinates: {self.bottom_left_pnt.x}, {self.bottom_left_pnt.y}" \
               f"and {self.upper_right_pnt.x}, {self.upper_right_pnt.y}"

    def is_inside(self) ->bool:
        pass