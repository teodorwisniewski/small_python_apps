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
        x_guess = input("Guess the point inside - x coordinate")
        y_guess = input("Guess the point inside - y coordinate")
        self.user_point = RandomPoint(x=x_guess, y=y_guess)

    def get_result(self):
        return self.bottom_left_pnt < self.user_point < self.upper_right_pnt



class RandomPoint:

    def __init__(self, x=None, y=None, min_x=0, min_y=0, delta_x=10, delta_y=10):
        if (x is None) or (y is None):
            self.x = random.randint(min_x, min_x+delta_x)
            self.y = random.randint(min_y, min_y+delta_y)
        else:
            self.x = x
            self.y = y

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)


if __name__ == "__main__":
    game = GeometryGame()
    game.run()