import random
import math

class Cities:
    def __init__(self, x=None, y=None):
        self.x = None
        self.y = None
        if x is not None:
            self.x = x
        else:
            self.x = int(random.random() * 200)
        if y is not None:
            self.y = y
        else:
            self.y = int(random.random() * 200)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def toDistance(self, Cities):
        xCoor = abs(self.getX() - Cities.getX())
        yCoor = abs(self.getY() - Cities.getY())
        distance = math.sqrt((xCoor * xCoor) + (yCoor * yCoor))
        return distance

    def __repr__(self):
        return str(self.getX()) + ", " + str(self.getY())