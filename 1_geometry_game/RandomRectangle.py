from RandomPoint import RandomPoint


class RandomRectangle:

    def __init__(self):
        self.bottom_left_pnt = RandomPoint()
        self.upper_right_pnt = RandomPoint(min_x=self.bottom_left_pnt.x+1,
                                     min_y=self.bottom_left_pnt.y+1)

    def __repr__(self):
        return f"Rectangle Coordinates: {self.bottom_left_pnt.x}, {self.bottom_left_pnt.y} " \
               f"and {self.upper_right_pnt.x}, {self.upper_right_pnt.y}"

    def is_inside(self, user_point: RandomPoint) ->bool:
        return self.bottom_left_pnt < user_point < self.upper_right_pnt