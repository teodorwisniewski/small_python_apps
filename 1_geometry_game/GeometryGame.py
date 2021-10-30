import random


class GeometryGame:

    def __init__(self):
        self.bottom_left_pnt = RandomPoint()
        self.upper_right_pnt = RandomPoint(min_x=self.bottom_left_pnt.x,
                                     min_y=self.bottom_left_pnt.y)

    def run(self) -> bool:
        self.guess()
        result = self.get_result()

        print(f"Your point is insede rectangle: {result}")
        return result

    def guess(self):
        x_guess = input("Guess the point inside - x coordinate: ")
        y_guess = input("Guess the point inside - y coordinate: ")
        self.user_point = RandomPoint(x=x_guess, y=y_guess)

    def get_result(self):
        return self.bottom_left_pnt < self.user_point < self.upper_right_pnt





