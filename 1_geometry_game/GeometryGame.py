import random


class GeometryGame:

    def __init__(self):
        self.bottom_left_pnt = RandomPoint()
        self.upper_right_pnt = RandomPoint(min_x=self.bottom_left_pnt.x,
                                     min_y=self.bottom_left_pnt.y)

    def run(self):
        pass

    def guess(self):
        pass

    def get_result(self):
        pass


class RandomPoint:

    def __init__(self, min_x=0, min_y=0, delta_x=10, delta_y=10):
        self.x = random.randint(min_x, min_x+delta_x)
        self.y = random.randint(min_y, min_y+delta_y)

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def __lt__(self, other):
        return (self.x < other.x) and (self.y < other.y)

if __name__ == "__main__":
    game = GeometryGame()
    game.run()