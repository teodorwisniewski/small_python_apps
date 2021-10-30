import random
from RandomPoint import RandomPoint
from RandomRectangle import RandomRectangle


class GeometryGame:

    def __init__(self):
        self.rectangle = RandomRectangle()
        print(self.rectangle)
        self.guess()
        result = self.rectangle.is_inside(self.user_point)
        print(f"Your point was inside rectangle: {result}")

    def guess(self):
        x_guess = input("Guess the point inside - x coordinate: ")
        y_guess = input("Guess the point inside - y coordinate: ")
        self.user_point = RandomPoint(x=float(x_guess), y=float(y_guess))






