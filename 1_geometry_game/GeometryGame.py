import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
from RandomPoint import RandomPoint
from RandomRectangle import RandomRectangle


class GeometryGame:

    def __init__(self):
        self.rectangle = RandomRectangle()
        print(self.rectangle)
        self.guess()
        self.result = self.rectangle.is_inside(self.user_point)
        print(f"Your point was inside rectangle: {self.result}")
        self.vizualize()

    def guess(self):
        x_guess = input("Guess the point inside - x coordinate: ")
        y_guess = input("Guess the point inside - y coordinate: ")
        self.user_point = RandomPoint(x=float(x_guess), y=float(y_guess))

    def vizualize(self):
        line_color = "green" if self.result else "red"
        fig, ax = plt.subplots()

        x_cor, y_cor = self.rectangle.bottom_left_pnt.get_cord()
        ax.add_patch(Rectangle((x_cor, y_cor), self.rectangle.width,
                     self.rectangle.heigth,
                     fc='none',
                     color=line_color,
                     linewidth=5,
                     ))
        ax.scatter([self.user_point.x], [self.user_point.y],s=80)
        plt.xlabel("X-AXIS")
        plt.ylabel("Y-AXIS")
        plt.title("Inside the rectagle Geometry game")
        plt.show()







