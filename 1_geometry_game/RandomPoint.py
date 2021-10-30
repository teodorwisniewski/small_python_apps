import random


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